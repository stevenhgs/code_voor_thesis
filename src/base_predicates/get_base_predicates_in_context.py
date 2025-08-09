from src.base_predicates.base_predicates import get_base_relation_name_to_relation_dict, get_objects_id_to_objects_and_all_objects
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from src.custom_classes.Relation import Relation


def get_context_to_all_objects_and_base_relation_with_context(input_file_names: list[str], xml_directory_path):
    base_relation_name_to_base_relations_with_context = dict()
    context_to_all_objects = dict()
    for input_file_name in input_file_names:
        object_id_to_object, all_objects = get_objects_id_to_objects_and_all_objects(input_file_name, xml_directory_path)
        base_relation_name_to_base_relations = get_base_relation_name_to_relation_dict(object_id_to_object)

        # prepare base relations
        for base_relation_name, base_relation in base_relation_name_to_base_relations.items():
            if base_relation_name_to_base_relations_with_context.get(base_relation_name) is None:
                base_relation_name_to_base_relations_with_context[base_relation_name] = Relation(base_relation_name,
                                                                                                 base_relation.arity,
                                                                                                 set())
            examples_in_context = set()
            for positive_example in base_relation.positive_examples:
                new_positive_example = tuple((input_file_name, object_id) for object_id in positive_example)
                examples_in_context.add(new_positive_example)
            base_relation_name_to_base_relations_with_context[base_relation_name].add_positive_examples(
                examples_in_context)

        # prepare all objects
        context_to_all_objects[input_file_name] = all_objects

    return context_to_all_objects, base_relation_name_to_base_relations_with_context
