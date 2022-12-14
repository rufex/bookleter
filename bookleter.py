import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter, PageObject
from pathlib import Path
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Provide the name or path to your original PDF file.')
args = parser.parse_args()

input_file =  Path(args.file)
input_suffix = input_file.suffix

if not input_file.is_file():
    raise Exception('File was not found. Check the name or path provided.')

if input_suffix.lower() != '.pdf':
    raise Exception('Your input file should be a have a pdf extension.')

folder = input_file.parent
input_name = input_file.stem
output_name = F"{input_name}_booklet{input_suffix}"
output_file = folder.joinpath(output_name)


def reorder_pages(pages_nr: int):

    if pages_nr % 4 == 0:
        pairs = int(pages_nr/2)
    else:
        raise Exception('The number of pages should be a divisible by 4.')

    pages = deque()

    for i in range(1,pages_nr+1):
        pages.append(i)

    ordered_list = []

    for i in range(0,pairs):
        pair = []
        # Pair
        if i % 2 == 0:
            pair.append(pages.pop())
            pair.append(pages.popleft())
        # Odd
        else:
            pair.append(pages.popleft())
            pair.append(pages.pop())
        ordered_list.append(pair)
    
    return ordered_list


def main():
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_file)

    pages_amount = pdf_reader.getNumPages()
    print('Number of Pages (Original File):',pages_amount)

    new_order = reorder_pages(pages_amount)
    print('Order in which the pages are going to be included:', new_order)

    page_size = pdf_reader.getPage(0).mediaBox.upperRight
    print('Page Size (First Page):', page_size)

    page_size_w = page_size[0]
    page_size_h = page_size[1]

    page_count = 0

    for pair in new_order:

        page_count += 1

        i_left = pair[0]-1
        i_right = pair[1]-1

        page_left = pdf_reader.getPage(i_left)
        page_right = pdf_reader.getPage(i_right)

        # Create Blank Page where we are going to render two pages on top of it
        merged = PageObject.createBlankPage(width=page_size_w*2, height=page_size_h)
 
        # Render left and right pages on the blank canvas
        merged.mergeTranslatedPage(page_left, 0, 0)
        merged.mergeTranslatedPage(page_right, page_size_w, 0)

        pdf_writer.addPage(merged)

    print('Number of Pages (Export File):',page_count)

    with open(output_file, 'wb') as F:
        pdf_writer.write(F)
        print('Done. PDF generated')


if __name__ == "__main__":
    main()
