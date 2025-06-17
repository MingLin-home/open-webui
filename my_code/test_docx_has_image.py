'''
pip install python-docx

On remote server:

docker pull fra.ocir.io/idqj093njucb/libreofficedocker/libreoffice-unoserver:3.19-e2eb67c
docker run -d -p 3001:2002 fra.ocir.io/idqj093njucb/libreofficedocker/libreoffice-unoserver:3.19-e2eb67c

On mac:
kubectl
'''
import os
import time
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def has_image_in_docx(docx_filename):
    if not docx_filename.lower().endswith('.docx'):
        raise ValueError("The input file must be a .docx file.")

    start_time = time.time()
    document = Document(docx_filename)
    
    rels = document.part.rels
    has_image = any(rel.target_ref for rel in rels.values() if rel.reltype == RT.IMAGE)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Time taken: {duration:.4f} seconds")
    return {'has_image': has_image, 'duration': duration}

# Example usage:
filename = '/Users/mmilin/tmp/Test Open-WebUI KnowledgeBase/sample.docx'
result = has_image_in_docx(filename)
print(result)
