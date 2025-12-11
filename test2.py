import requests
from tutor_agent import Agent
from context import content


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


# def test(url,niveau):
#     ###Cette fonction utilise les fonction RecupPdf e PdfToTexte et donne en sortie la reponse du llm apres qu'il lui ai envoyer le contenu du pdf et mis le bon niveau

#     #Prend en argument l'url et telecharge le pdf souys le nom "article.pdf"
#     RecupPdf(url)
#     #recupere le contenu du pdf en texte et le met dans la variable ContenuPdf
#     ContenuPdf = PdfToText("article.pdf")
#     #configure le bon prompt system en fonction du niveau mis en argument
#     promptF = GroqAgent.AjoutPrompt(niveau,content)
#     # Prend en argument le prompt system adapter au niveau et le contenu du pdf du pdf afin de faire le resumer (ils ait deja qu'il doit faire un resumer car c'est dnas le prompt system)
#     return GroqAgent.ask(ContenuPdf,promptF)

RecupPdf("https://arxiv.org/pdf/2512.09853")
ContenuPdf = PdfToText("article.pdf")
promptF = GroqAgent.AjoutPrompt("avancé",content)
reponse = GroqAgent.ask(ContenuPdf,promptF)
print(reponse)

# reponse = test("https://arxiv.org/pdf/2512.09853","avancé")
# print(reponse)
