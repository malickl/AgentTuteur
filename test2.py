import requests
from APIgroq import Agent
from Prompt import content


GroqAgent = Agent()

def RecupPdf(url):
    URL = url
    response = requests.get(URL)
    open("article.pdf", "wb").write(response.content)


def PdfToText(pdf):
    import fitz

    # Open a PDF file
    pdf_document = pdf
    doc = fitz.open(pdf_document)

    # Initialize an empty string to store extracted text
    extracted_text = ""

    # Iterate through each page and extract text
    for page_num in range(doc.page_count):
        page = doc[page_num]
        extracted_text += page.get_text()
        
    # Close the PDF document
    doc.close()

    return extracted_text



RecupPdf("https://arxiv.org/pdf/2512.09853")
ContenuPdf = PdfToText("article.pdf")
promptF = GroqAgent.AjoutPrompt("avancé",content)
reponse = GroqAgent.ask(ContenuPdf,promptF)
print(reponse)
