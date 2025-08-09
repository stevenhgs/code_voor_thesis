from src.pdf_to_xml.pdf_to_xml import pdf_to_xml
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from src.base_predicates.base_predicates import get_base_relation_name_to_relation_dict
from src.find_complex_rule_examples.find_complex_rule_examples import find_complex_rule_examples
from src.custom_classes.Literal import Literal
from src.custom_classes.Rule import Rule
from src.get_sequential_order.get_sequential_order import get_sequential_order


def get_complex_rule_examples_from_pdf(input_file_name, head_and_body_rules):
    pdf_input_path = f"../../data/input/{input_file_name}.pdf"
    pdf_to_xml(pdf_input_path)
    xml_input_path = f"../../data/output/{input_file_name}.xml"
    object_id_to_object = get_objects_from_xml_file_path(xml_input_path)

    # double shape problem
    new_object_id_to_object = dict()
    seen = set()
    for object_id, object in object_id_to_object.items():
        if object["type"] == "curve":
            if tuple(object["pts"]) not in seen:
                new_object_id_to_object[object_id] = object
                seen.add(tuple(object["pts"]))
        else:
            new_object_id_to_object[object_id] = object

    object_id_to_object = new_object_id_to_object
    all_objects = set(object_id_to_object.keys())
    base_relation_name_to_base_relations = get_base_relation_name_to_relation_dict(object_id_to_object)

    for _, base_relation in base_relation_name_to_base_relations.items():
        print(base_relation)

    print()
    complex_relation_name_to_complex_relation = find_complex_rule_examples(head_and_body_rules, base_relation_name_to_base_relations, all_objects)
    for _, complex_relation in complex_relation_name_to_complex_relation.items():
        print(complex_relation)

    sequential_order = get_sequential_order(all_objects, complex_relation_name_to_complex_relation)
    print(f'sequential order of elements:')
    print(sequential_order)


if __name__ == "__main__":
    rules = [
        Rule(Literal(False, "Together", 2, [0, 1]), [Literal(False, "XDimCovers", 2, [1, 0]), Literal(False, "YDimCovers", 2, [1, 0])]),
        Rule(Literal(False, "Together", 2, [0, 1]), [Literal(False, "AtTipOfArrow", 2, [0, 1])]),
        Rule(Literal(False, "DirectlyFollows", 2, [0, 1]), [Literal(False, "AtBaseOfArrow", 2, [1, 2]), Literal(False, "AtTipOfArrow", 2, [0, 2])])
    ]
    get_complex_rule_examples_from_pdf("five_way_process", rules)