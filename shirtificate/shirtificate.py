from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 20, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=10, y=60, w=190)

pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)

pdf.text(x=60, y=140, text=f"{name} took CS50")

pdf.output("shirtificate.pdf")
