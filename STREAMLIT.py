import re
import spacy
import streamlit as st
import PyPDF2
from transformers import pipeline
from transformers import BartTokenizer


def clean_text(text):
    text = re.sub(r"['’]", '', text)
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    cleaned_text = ' '.join(tokens)
    cleaned_text = cleaned_text.lower().strip()
    return cleaned_text


def extract_text_from_pdf(uploaded_files):
    reader = PyPDF2.PdfReader(uploaded_files)
    text = ''
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text


def split_text(text, max_length=1024):
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    tokens = tokenizer.encode(text)
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    return [tokenizer.decode(chunk) for chunk in chunks]


nlp = spacy.load("pl_core_news_sm")
uploaded_files = st.file_uploader("Wybierz plik pdf", ['pdf'])  # okienko na stronie do wrzucenia pliku

if uploaded_files:
    pdf_text = extract_text_from_pdf(uploaded_files)  # wyekstrahuj tekst z pliku pdf
    clean_text = clean_text(pdf_text)  # wyczyść tekst
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")  # tokenizuj tekst
    tokens = tokenizer.encode(clean_text, return_tensors='pt')  # zwróć tensory
    st.write("Number of tokens:", len(tokens[0]))
    text_chunks = split_text(clean_text)
    for chunk in text_chunks:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        st.write(summary[0]['summary_text'])