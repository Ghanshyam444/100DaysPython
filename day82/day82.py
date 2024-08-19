# Merge PDF Exercise
# Merge two PDF files into a single PDF file
# using pypdf2 

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

#for pdf in ["day82/file1.pdf", "day82/file2.pdf"]:
 #   merger.append(pdf)
  
files = [ file for file in os.listdir() if file.endswith(".pdf") ]

for pdf in files:
    merger.append(pdf)  
  
merger.write("merged_pdf.pdf")
merger.close()
