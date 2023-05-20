import os
import pandas as pd
import PyPDF2
import hashlib

SENT_FOLDER = ""
SIGNED_FOLDER = ""

def string_to_hash(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()

def extract_pdf_content(file_path):
    content = ""
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            content += pdf_reader.pages[page].extract_text()

    return content.strip()

def compare_pdfs(signed_folder, sent_folder):
    signed_files = [file for file in os.listdir(signed_folder) if file.endswith('.pdf')]
    sent_files = [file for file in os.listdir(sent_folder) if file.endswith('.pdf')]

    data = []

    # Add matches
    for sent_file_name in sent_files:
        for signed_file_name in signed_files:

            if sent_file_name.replace(" ", "_") == signed_file_name.replace(" ", "_"):
                sent_files.remove(sent_file_name)
                signed_files.remove(signed_file_name)

                sent_file_path = os.path.join(sent_folder, sent_file_name)
                sent_file_hash = string_to_hash(extract_pdf_content(sent_file_path))

                signed_file_path = os.path.join(signed_folder, signed_file_name)
                signed_file_hash = string_to_hash(extract_pdf_content(signed_file_path))
                
                data.append((sent_file_name, sent_file_hash, signed_file_name, signed_file_hash))

    # Add sent files without a match
    for sent_file_name in sent_files:
        sent_file_path = os.path.join(sent_folder, sent_file_name)
        sent_file_hash = string_to_hash(extract_pdf_content(sent_file_path))
        data.append((sent_file_name, sent_file_hash, None, None))

    # Add signed files without a match
    for signed_file_name in signed_files:
        signed_file_path = os.path.join(signed_folder, signed_file_name)
        signed_file_hash = string_to_hash(extract_pdf_content(signed_file_path))
        data.append((None, None, signed_file_name, signed_file_hash))

    df = pd.DataFrame(data, columns=['Sent', 'Sent_Hash', 'Signed', 'Signed_Hash'])
    return df

if __name__ == '__main__':
    result = compare_pdfs(SIGNED_FOLDER, SENT_FOLDER)
    result.to_csv('result.csv', index=False)

    