from src.pdf_to_xml.pdf_to_xml import pdf_to_xml
from src.drawing_on_pdf.draw_object_ids_on_pdf import draw_object_ids_on_pdfs, draw_object_ids_on_pdfs_multiple_pages


if __name__ == "__main__":
    # pdf input path
    pdf_input_directory = "../data/dataset/"
    pdf_file_names = ["short"]
    # xml output path
    xml_output_directory = "./xmls/"
    # output path to store pdfs with object ids
    drawn_pdf_file_output_directory = "./object_id_on_pdf/"

    # convert to xmls
    for pdf_file_name in pdf_file_names:
        full_pdf_input_file_path = pdf_input_directory + pdf_file_name + ".pdf"
        nb_pages = pdf_to_xml(full_pdf_input_file_path, xml_output_directory)
        if nb_pages == 1:
            draw_object_ids_on_pdfs(pdf_input_directory,
                                    xml_output_directory,
                                    drawn_pdf_file_output_directory,
                                    pdf_file_name)
        else:
            draw_object_ids_on_pdfs_multiple_pages(pdf_input_directory,
                                                   xml_output_directory,
                                                   drawn_pdf_file_output_directory,
                                                   pdf_file_name,
                                                   nb_pages)


