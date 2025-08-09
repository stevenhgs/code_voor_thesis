from src.base_predicates.get_base_predicates_in_context import get_context_to_all_objects_and_base_relation_with_context
from complete_pipeline.configurations.thesis_example import config
from src.mfoil.mfoil_with_context import mfoil_with_context
from src.custom_classes.Relation import Relation


def get_target_relation_name_to_target_relations_with_context(input_file_names, complex_relation_config):
    target_relation_name_to_target_relations_with_context = dict()
    for input_file_name in input_file_names:

        # prepare target relation
        for target_relation_name, target_relation in complex_relation_config[input_file_name].items():
            if target_relation_name_to_target_relations_with_context.get(target_relation_name) is None:
                target_relation_name_to_target_relations_with_context[target_relation_name] = Relation(target_relation_name, target_relation.arity, set())
            examples_in_context = set()
            for positive_example in target_relation.positive_examples:
                new_positive_example = tuple((input_file_name, object_id) for object_id in positive_example)
                examples_in_context.add(new_positive_example)
            target_relation_name_to_target_relations_with_context[target_relation_name].add_positive_examples(examples_in_context)

    return target_relation_name_to_target_relations_with_context


def learn_rules_from_pdf_in_context(input_file_names: list[str], xml_directory_path, complex_relation_config, beam_size, min_significance):
    """
    IMPORTANT that the input_file_name is the same as the config.
    """
    context_to_all_objects, base_relation_name_to_base_relations_with_context = get_context_to_all_objects_and_base_relation_with_context(input_file_names, xml_directory_path)
    target_relation_name_to_target_relations_with_context = get_target_relation_name_to_target_relations_with_context(input_file_names, complex_relation_config)

    # learn rules
    all_learned_rules = []
    for target_relation_name, target_relation in target_relation_name_to_target_relations_with_context.items():
        learned_rules = mfoil_with_context(target_relation, base_relation_name_to_base_relations_with_context, context_to_all_objects, beam_size, min_significance)
        all_learned_rules += learned_rules
    return all_learned_rules


if __name__ == "__main__":
    xml_directory_path = "../../data/output/"
    file_names = ["tree_example", "bullet_points"]
    complex_relation_config = config
    learned_rules = learn_rules_from_pdf_in_context(file_names, xml_directory_path, complex_relation_config, beam_size=5, min_significance=0)
    for rule in learned_rules:
        print(rule)
