from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="L", unit="mm", format="A4")  # landscape
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=15)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=15, txt=row["Topic"], align="L", ln=1)

    pdf.line(11,20,200,20)

pdf.output("output.pdf")
