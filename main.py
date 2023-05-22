from fpdf import FPDF
from pathlib import Path
import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1', engine="openpyxl")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, align='L', txt=f"Invoice nr. {invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")
