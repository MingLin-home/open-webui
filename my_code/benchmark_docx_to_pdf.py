import os, sys
import requests
import base64
import time
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def has_image_in_docx(docx_filename):
    if not docx_filename.lower().endswith('.docx'):
        raise ValueError("The input file must be a .docx file.")

    document = Document(docx_filename)
    
    rels = document.part.rels
    has_image = any(rel.target_ref for rel in rels.values() if rel.reltype == RT.IMAGE)
    return has_image

def docx_to_pdf_base64(docx_path):
    url = 'http://127.0.0.1:2004/request'
    with open(docx_path, 'rb') as f:
        files = {'file': (docx_path, f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
        data = {'convert-to': 'pdf'}
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        # The response content is the PDF file
        pdf_bytes = response.content
        b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        return b64_pdf
      
def save_base64_as_pdf(base64_str, pdf_path):
    pdf_bytes = base64.b64decode(base64_str)
    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)
        
if __name__ == "__main__":
    # input_fn = sys.argv[1]
    # output_fn = sys.argv[2]
    input_fn = '/Users/mmilin/tmp/Test Open-WebUI KnowledgeBase/sample.docx'
    
    time_start = time.perf_counter()
    has_image = has_image_in_docx(docx_filename=input_fn)    
    time_end = time.perf_counter()
    elasp_time_has_image = time_end - time_start
    
    time_start = time.perf_counter()
    docx_to_pdf_base64(docx_path=input_fn)
    time_end = time.perf_counter()
    docx_to_pdf_base64 = time_end - time_start
    
    print(f"elasp_time_has_image={elasp_time_has_image}, docx_to_pdf_base64={docx_to_pdf_base64}")