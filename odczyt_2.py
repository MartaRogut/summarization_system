import PyPDF2
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Użycie
pdf_text = extract_text_from_pdf('pdf/tekst.pdf')
#print(pdf_text)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print(summarizer("""Przerażające zachowania człowieka wobec drugiej jednostki w czasach wojny ukazał Tadeusz 
Borowski w utworze pt. ,, Proszę państwa do gazu ,,, gdzie została pokazana rzeczywistość obozowa.  
Jedną ze wstrząsających scen jaką opisał Borowski jest ukazanie dziecka, które biegnie za swoją 
matką krzycząc ,, mamo,,. Kobieta nie przyznaje się do własnego stworzenia, ucieka zakrywając 
twarz rękoma. Ukazana została także dziewczynka bez nogi trzymają ca się za ręce, łzy ciekną jej po 
twarzy, k rzyczy ,, boli,,, lecz więźniowie cisną ją na auto. Te drastyczne sceny pokazują człowieka w 
sytuacji ekstremalnej, który jest pozbawiony uczuć, bezlitosny, odczłowieczony, celem jednostki jest 
przeżycie kosztem d rugiego człowieka.  """, max_length=130, min_length=3, do_sample=False))

