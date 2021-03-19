import os
import glob
from tika import parser

input_folder='/home/perennial/Hemlata-Python-Trainning/parser/smaple-docs'
for input_files in glob.glob(os.path.join(input_folder,'*.pdf')):
    print(input_files)
    parserPDF=parser.from_file(input_files)
    print("\n printing metadata\n\n",parserPDF)

    #extract content from pdf file
    pdfCont=parserPDF['content']
    splited=pdfCont.splitlines()
    print("\nprinting contents of file\n\n",splited)