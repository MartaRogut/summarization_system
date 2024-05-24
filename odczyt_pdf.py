import os
import PyPDF2

pdf_path = r'C:\Users\48534\PycharmProjects\pdf_sum\Matematyka.pdf'

# Sprawdź, czy plik istnieje
if not os.path.exists(pdf_path):
    print(f"Plik PDF o ścieżce '{pdf_path}' nie został znaleziony.")
else:
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            pdf_text = ""

            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                pdf_text += page.extract_text()

        print(pdf_text)

    except FileNotFoundError:
        print(f"Plik PDF o ścieżce '{pdf_path}' nie został znaleziony.")