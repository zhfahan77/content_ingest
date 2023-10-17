import requests
import PyPDF2
import io

def scrape_pdf(pdf_url):
    response = requests.get(pdf_url)

    if response.status_code == 200:
        pdf_file = io.BytesIO(response.content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        info = pdf_reader.metadata

        extracted_text = ""

        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        data = {
            'title': info.title,
            'body': extracted_text
        }
        return data
