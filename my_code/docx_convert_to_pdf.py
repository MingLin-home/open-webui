import requests
import base64

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
              
filename = '/Users/mmilin/tmp/Test Open-WebUI KnowledgeBase/sample.docx'
pdf_path = '/Users/mmilin/tmp/debug/result.pdf'


pdf_b64 = docx_to_pdf_base64(filename)
# print(pdf_b64)  # This is your PDF as a base64 string
save_base64_as_pdf(pdf_b64, pdf_path)
print(f"PDF saved to {pdf_path}")