from PyPDF2 import PdfReader
import base64
from mimetypes import guess_type
def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    count = len(pdf_reader.pages)
    for i in range(count):
        page = pdf_reader.pages[0]
        text += page.extract_text()
    return text

def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"