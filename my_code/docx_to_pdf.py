'''
pip install python-docx

Import onlyoffice document server image into docker

docker load < onlyoffice_documentserver.tar

Run onlyoffice server (https://helpcenter.onlyoffice.com/docs/installation/docs-community-install-docker.aspx):

PORT_NUMBER=80
docker run -i -t -d -p ${PORT_NUMBER}:80 --restart=always -e JWT_ENABLED=false -e JWT_SECRET=my_jwt_secret onlyoffice/documentserver

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
