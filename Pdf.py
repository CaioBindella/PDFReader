import PyPDF2
import json
import os

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

#Caminho do PDF
file_path = '/Users/caiobindella/Downloads/trabalho.pdf'
text = read_pdf(file_path)
print("Texto extraído do PDF:\n", text)

# Supondo que o texto não está em formato JSON e precisamos estruturá-lo
data = {
    "content": text
    # Adicione aqui outras chaves/valores conforme necessário
}

# Converter o dicionário para JSON sem escapar caracteres Unicode
jsonPDF = json.dumps(data, ensure_ascii=False, indent=4)
print("JSON formatado:\n", jsonPDF)

# Gerar o caminho do novo arquivo JSON
json_file_path = os.path.splitext(file_path)[0] + '.json'

# Gravando a string JSON em um arquivo
with open(json_file_path, "w", encoding='utf-8') as arquivo:
    arquivo.write(jsonPDF)

print(f"JSON salvo em: {json_file_path}")
