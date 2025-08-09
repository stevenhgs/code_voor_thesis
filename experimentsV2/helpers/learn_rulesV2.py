from src.pipeline.learn_rules_from_pdf_mfoil_context import learn_rules_from_pdf_in_context
# NOTE: make sure to put the right config
from src.base_predicates.base_predicates import get_objects_id_to_objects_and_all_objects, get_base_relation_name_to_relation_dict
from src.find_complex_rule_examples.find_complex_rule_examples import find_complex_rule_examples
from complete_pipeline.configurations.exp_configuration import config


def learn_rules_and_add_train_accuracy_v2(pdf_file_names, xml_output_directory, config, beam_size, min_significance, target_relation_name):
    # print("learning rules...")
    if len(pdf_file_names) == 0:
        return []
    reformed_config = dict()
    for key, relation_annotations in config.items():
        reformed_config[key] = {target_relation_name: relation_annotations[target_relation_name]}
    print(f'{target_relation_name}: ')
    learned_rules = learn_rules_from_pdf_in_context(pdf_file_names, xml_output_directory, reformed_config, beam_size, min_significance)
    for file_name in pdf_file_names:
        object_id_to_object, all_objects = get_objects_id_to_objects_and_all_objects(file_name, xml_output_directory)
        base_relation_name_to_relation = get_base_relation_name_to_relation_dict(object_id_to_object)
        for rule in learned_rules:
            if rule.mfoil_significance < min_significance:
                continue
            complex_relation_name = rule.head.name
            relation_name_to_relation = find_complex_rule_examples([rule], base_relation_name_to_relation, all_objects)
            positive_examples = relation_name_to_relation[complex_relation_name].positive_examples
            for positive_example in positive_examples:
                if positive_example in config[file_name][complex_relation_name].positive_examples:
                    rule.nb_positive_train += 1
                else:
                    rule.nb_negative_train += 1

    return learned_rules


if __name__ == "__main__":
    pdf_file_names = ["tree_example"]
    # xml output path
    xml_output_directory = "./xmls/"
    learned_rules = learn_rules_and_add_train_accuracy(pdf_file_names, xml_output_directory, config, 10, 0, "DirectlyFollows")
    for rule in learned_rules:
        print(rule)
        print(repr(rule))
