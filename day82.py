# Merge PDF Exercise
# Merge two PDF files into a single PDF file
# using pypdf2 

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

#for pdf in ["day82/file1.pdf", "day82/file2.pdf"]:
 #   merger.append(pdf)
  
files = [ file for file in os.listdir("day82") if file.endswith(".pdf") ]

for pdf in files:
    merger.append(pdf)    
merger.write("day82/output.pdf")
merger.close()
