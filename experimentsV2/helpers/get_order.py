from src.base_predicates.base_predicates import get_objects_id_to_objects_and_all_objects
from src.get_sequential_order.get_sequential_order import get_sequential_order
from src.custom_classes.Relation import Relation

def get_order_score(relation_to_found_examples, relation_to_true_examples, file_name, xml_output_directory):
    object_id_to_object, all_objects = get_objects_id_to_objects_and_all_objects(file_name, xml_output_directory)
    relation_name_to_relation = dict()
    for relation, found_examples in relation_to_found_examples.items():
        relation_name_to_relation[relation] = Relation(relation, 2, found_examples)
    sequential_order_found_examples, all_included_found = get_sequential_order(all_objects, relation_name_to_relation)
    relation_name_to_relation = dict()
    for relation, true_examples in relation_to_true_examples.items():
        relation_name_to_relation[relation] = Relation(relation, 2, true_examples)
    sequential_order_true_examples, all_included_true = get_sequential_order(all_objects, relation_name_to_relation)

    contradictions = list()
    for examples in relation_to_found_examples['Together']:
        if examples in relation_to_found_examples['DirectlyFollows']:
            contradictions.append(examples)
        if (examples[1], examples[0]) in relation_to_found_examples['DirectlyFollows']:
            contradictions.append(examples)

    data = dict()
    data['sequential_order_found_examples'] = sequential_order_found_examples
    data['sequential_order_true_examples'] = sequential_order_true_examples
    data['all_included_found'] = all_included_found
    data['all_included_true'] = all_included_found
    data['contradictions'] = contradictions
    return data