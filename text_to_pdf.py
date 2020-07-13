# fpdf

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=15)
f = open("sample_text.txt", "r")
for line in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

pdf.output("sample_pdf.python")