import src.pdf_to_xml.pdf2txt as pdf2txt


def pdf_to_xml(input_file_path: str, output_file_path=None):
    input_file_name = input_file_path.split('/')[-1].split('.')[0]
    # get output file name from input file name
    if output_file_path is None:
        output_file_path = "../../data/output/"
    output_file_name = output_file_path + input_file_name + ".xml"
    arguments = ['dummy', '-t', 'xml', '-o', f'{output_file_name}', f'{input_file_path}']
    pdf2txt.main(arguments)

    # check if multiple pages
    with open(output_file_name, encoding="utf8") as file:
        xml_data = file.read()
        nb_pages = xml_data.count("</page>")
    if nb_pages == 1:
        return nb_pages
    header = '<?xml version="1.0" encoding="utf-8" ?>\n<pages>\n'
    xml_data_split_on_header = xml_data.split(header)
    xml_data_without_header = xml_data_split_on_header[-1]
    counter = 0
    for page_xml_data in xml_data_without_header.split("</page>\n")[:-1]:
        output_xml_page_file_path_ = output_file_path + f"{input_file_name}_{counter}" + ".xml"
        new_xml_data = header + page_xml_data + "</page>\n</pages>"
        with open(output_xml_page_file_path_, "w+", encoding="utf8") as f:
            f.write(new_xml_data)
        counter += 1
    return nb_pages
