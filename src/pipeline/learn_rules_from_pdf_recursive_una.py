from src.pdf_to_xml.pdf_to_xml import pdf_to_xml
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from src.base_predicates.base_predicates import get_base_relation_name_to_relation_dict
from src.complex_relation_configs.complex_relation_configs import config
from src.foil.foil_multi_development_recursion_una import foil_multi_development_recursion_una

import time


def learn_rules_from_pdf(input_file_name):
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
    base_relation_name_to_base_relations = get_base_relation_name_to_relation_dict(object_id_to_object)
    all_objects = set(object_id_to_object.keys())

    print(f'{all_objects=}')
    for base_relation_name, base_relation in base_relation_name_to_base_relations.items():
        print(base_relation)

    for target_relation_name, target_relation in config[input_file_name].items():
        rule_groups = foil_multi_development_recursion_una(target_relation, base_relation_name_to_base_relations, all_objects)
        print(f'\n{target_relation_name=}: {len(rule_groups)} different groups')
        for rule_group in rule_groups:
            print(f'rule_group:')
            head, learned_rules  = rule_group
            for learned_rule in learned_rules:
                print(f'{head} <-- {" ∧ ".join([str(literal) for literal in learned_rule])}')
        print(f'\n{target_relation_name=}: {len(rule_groups)} different groups')


if __name__ == "__main__":
    start = time.time()
    learn_rules_from_pdf("tree_example")
    end = time.time()
    print(end - start)
