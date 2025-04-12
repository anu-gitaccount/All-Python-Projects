
# python3 -m pip install pytube --break-system-packages

import sys
import os
import PyPDF2

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        
        merger.append(file)

    merger.write("CombinedPdf.pdf")


    

