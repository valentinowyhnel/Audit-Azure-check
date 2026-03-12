from docx import Document
import os

doc_path = r"C:\Users\dell\Downloads\Audit avancé Active Directory + Azure _ repository GitHub clé-en-main.docx"
output_path = r"C:\Users\dell\.gemini\antigravity\scratch\content.txt"

if os.path.exists(doc_path):
    doc = Document(doc_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_text))
    print(f"Success: Content written to {output_path}")
else:
    print(f"Error: File not found at {doc_path}")
