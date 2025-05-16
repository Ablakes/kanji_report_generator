import json
from fpdf import FPDF

def load_user_data(email, filename="../kanji_crow/dummy_cache/user_dummy_data.json"):
    # Open and read the user dummy data json file
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        user = data.get(email)
        if not user:
            raise ValueError(f"No user found with email: {email}")
        kanji_list = user["kanji_data"]["known"]
        if not kanji_list:
            raise ValueError(f"No known kanji found for user: {email}")
        return kanji_list
    
    # If there are errors print them and return an empty array
    except Exception as error:
        print(f"Error: {error}")
        return []

# Use FPDF to format the report as a pdf
def generate_pdf(kanji_list, email):
    pdf = FPDF()
    pdf.add_page()

    # Add Kanji-supporting font
    pdf.add_font("NotoSansJP", "", "NotoSansJP-VariableFont_wght.ttf", uni=True)
    pdf.set_font("NotoSansJP", size=12)

    pdf.cell(200, 10, txt=f"Kanji Report for {email}", ln=True, align='C')
    pdf.ln(10)

    # Header formatting for FPDF
    pdf.set_font("NotoSansJP", size=10)
    pdf.cell(20, 10, "Kanji", 1)
    pdf.cell(40, 10, "Heisig", 1)
    pdf.cell(15, 10, "JLPT", 1)
    pdf.cell(115, 10, "Meanings", 1)
    pdf.ln()

    # Table body formatting for FPDF
    for k in kanji_list:
        pdf.cell(20, 10, k.get("kanji", ""), 1)
        pdf.cell(40, 10, k.get("heisig_en", ""), 1)
        pdf.cell(15, 10, str(k.get("jlpt", "")), 1)
        pdf.cell(115, 10, "; ".join(k.get("meanings", [])), 1)
        pdf.ln()

    # Replace '@' in the filename
    filename = f"kanji_report_{email.replace('@', '_at_')}.pdf"
    pdf.output(filename)
    print(f"PDF saved as: {filename}")


if __name__ == "__main__":
    email = input("Enter the user's email: ").strip()
    kanji_list = load_user_data(email)
    if kanji_list:
        generate_pdf(kanji_list, email)
