# Bookleter

> Are you looking to create a booklet or zine ?

## Description

Python script to generate an ordered, ready-to-print booklet/zine.

The order of the pages as you visualize them, or you want to display them, is no the same order in which the pages should be arrarnged to be printed as a booklet. Get your PDF is "naturally" ordered pages, re-arrange them in the right order to be printed, and also combine each pair of pages (originally in A5/A4 size) into one new A4.

As an example, if you originally have a PDF with 20 pages, you will get a PDF (as mentioned, ready-to-print) with 10 A4 pages. You will most likely print this 10 pages in both sides of each page, so you will get a fisical booklet with 5 A4 pages in the end.

This is script will also check that the amount of pages in your original PDF has the right amount of pages in the first place (which has to be a multiple of 4, following the previous example).

## How it works

- It will create empty A4 pages, and render two pages in each of them. One on the left, and one of the right. Two original portrait-oriented pages will be included in one new A4 landscape-oriented page.

## Setup

## How to use it