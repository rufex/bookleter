from PyPDF2 import PdfFileReader, PdfFileWriter, PageObject
from pathlib import Path

folder = Path(__file__).parent
output = folder.joinpath('output.pdf')

def main():
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader('input.pdf')

    pages_amount = pdf_reader.getNumPages()
    print('Number of Pages (Original File):',pages_amount)

    page_size = pdf_reader.getPage(0).mediaBox.upperRight
    print('Page Size (First Page):', page_size)

    page_size_w = page_size[0]
    page_size_h = page_size[1]

    page_count = 0

    for i in range(0, pages_amount, 2):
        page_count += 1

        page_left = pdf_reader.getPage(i)
        page_right = pdf_reader.getPage(i+1)

        # Create Blank Page where we are going to render two pages on top of it
        merged = PageObject.createBlankPage(width=page_size_w*2, height=page_size_h)
 
        # Render left and right pages on the blank canvas
        merged.mergeTranslatedPage(page_left, 0, 0)
        merged.mergeTranslatedPage(page_right, page_size_w, 0)

        pdf_writer.addPage(merged)

    print('Number of Pages (Export File):',page_count)

    with open(output, 'wb') as F:
        pdf_writer.write(F)
        print('Done. PDF generated')

if __name__ == "__main__":
    main()
