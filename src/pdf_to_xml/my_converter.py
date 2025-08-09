import pdfminer
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from pdfminer.converter import XMLConverter
from io import BytesIO
from io import StringIO

# Specify the PDF file
input_pdf = "..//..//data//input//dummy.pdf"

# Specify the output XML file
output_xml = "output.xml"

# Configure the LAParams for layout analysis
laparams = LAParams()

# Open the input and output files
with open(input_pdf, "rb") as pdf_file, open(output_xml, "wb") as xml_file:
    # Create a StringIO to capture the XML
    output_stream = BytesIO()

    # Extract text and write to the StringIO as XML
    extract_text_to_fp(pdf_file, output_stream, laparams=laparams, output_type='xml')

    # Write the XML to the output file
    xml_file.write(output_stream.getvalue())