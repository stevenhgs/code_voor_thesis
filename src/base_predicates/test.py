from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from base_predicates import get_base_predicates_from_objects
from src.arrow_recognition.arrow_recognition import find_arrow_from_list_of_points

if __name__ == "__main__":
    object_id_to_object = get_objects_from_xml_file_path("../../data/output/tree_example.xml")
    for key, val in object_id_to_object.items():
        print(f'{key}: {val}')
    print()
    base_predicates = get_base_predicates_from_objects(object_id_to_object)
    for key, val in base_predicates.items():
        print(f'{key}: {val}')
    print("\n\n\n")
    for object_id, object in object_id_to_object.items():
        if object["type"] == "curve":
            if len(object["pts"]) == 7:
                print(object["pts"])
                tip_of_arrow, base_of_arrow = find_arrow_from_list_of_points(object["pts"])
                print(tip_of_arrow)
                print(base_of_arrow)
