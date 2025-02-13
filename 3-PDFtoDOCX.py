import sys
from pdf2docx import Converter

if len(sys.argv) != 2:
	print("Uso: py 3-PDFtoDOCX.py <PDF>")
	sys.exit(1)
pdf_path = sys.argv[1]
output_path = pdf_path.rsplit('.', 1)[0] + '.docx'
cv = Converter(pdf_path)
cv.convert(output_path)
cv.close()