import base64
import json
import requests

def docx_to_pdf_base64(docx_path: str,
                       server_url: str = "http://localhost",
                       server_port: int = 80) -> str:
    """
    Convert a local .docx file to PDF using OnlyOffice Document Server
    and return the PDF as a base64‐encoded string.

    Args:
      docx_path:     Path to the local .docx file.
      server_url:    Base URL of the document server (default http://localhost).
      server_port:   Port of the document server (default 80).

    Returns:
      A base64 string containing the converted PDF data.

    Raises:
      RuntimeError if the conversion request fails.
    """
    # 1) Read and base64‐encode the source .docx
    with open(docx_path, "rb") as f:
        docx_bytes = f.read()
    b64_docx = base64.b64encode(docx_bytes).decode("utf-8")

    # 2) Build the JSON payload for the conversion API
    payload = {
        "async": False,
        "filetype": "docx",
        "outputtype": "pdf",
        "title": docx_path.split("/")[-1],
        # supply the file itself as base64
        "file": b64_docx
    }

    # 3) POST to ConvertService
    convert_url = f"{server_url}:{server_port}/ConvertService"
    headers = {"Content-Type": "application/json"}
    resp = requests.post(convert_url, headers=headers, data=json.dumps(payload))

    # 4) Check for errors
    if resp.status_code != 200:
        raise RuntimeError(f"Conversion failed: {resp.status_code} {resp.text}")

    # 5) Parse JSON and extract the base64 PDF
    result = resp.json()
    if "file" not in result:
        raise RuntimeError(f"Unexpected response format: {result}")

    return result["file"]


if __name__ == "__main__":
    # Example usage:
    filename = '/Users/mmilin/tmp/Test Open-WebUI KnowledgeBase/sample.docx'
    pdf_b64 = docx_to_pdf_base64(filename)
    print("PDF base64 length:", len(pdf_b64))
    # If you want to decode and save it:
    with open("out.pdf", "wb") as f:
        f.write(base64.b64decode(pdf_b64))
    print("Saved out.pdf")