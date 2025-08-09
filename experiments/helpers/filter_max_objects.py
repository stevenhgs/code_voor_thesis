import os
from src.base_predicates.base_predicates import get_objects_id_to_objects_and_all_objects


def filter_max_objects(all_pdf_names, xml_path, max_nb_objects):
    filtered_pdf_names = []
    for file_name in all_pdf_names:
        _, all_objects = get_objects_id_to_objects_and_all_objects(file_name, xml_path)
        if len(all_objects) <= max_nb_objects:
            filtered_pdf_names.append(file_name)
    return filtered_pdf_names


if __name__ == "__main__":
    name = "BS10"
    xml_path = './../data/xmls/'
    input_xml_path = xml_path + name + '/'
    nb_pages = len(os.listdir(input_xml_path)) - 1
    all_pdf_file_names = [f'{name}_{i}' for i in range(nb_pages)]
    filtered = filter_max_objects(all_pdf_file_names, input_xml_path, 35)
    print(len(all_pdf_file_names), all_pdf_file_names)
    print(len(filtered), filtered)
