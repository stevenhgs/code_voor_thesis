from src.custom_classes.Relation import Relation
from src.custom_classes.Literal import Literal
from src.custom_classes.Rule import Rule
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from src.base_predicates.base_predicates import get_objects_id_to_objects_and_all_objects, get_base_relation_name_to_relation_dict
from src.find_complex_rule_examples.find_complex_rule_examples import find_complex_rule_examples
from collections import defaultdict
from math import inf
from random import random


def get_heuristic_values_my_heuristic(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2**nb_objects)
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    heuristic3 = nb_objects
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic1, heuristic2, -heuristic3)

def get_heuristic_values_step2_step1(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2**nb_objects)
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic2, heuristic2, heuristic1)

def get_heuristic_values_step2_step3(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic3 = nb_objects
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic2, heuristic2, -heuristic3)


def get_heuristic_values_step2(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic2, heuristic2, heuristic2)

def get_heuristic_values_my_heuristic_only_first(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2**nb_objects)
    return (heuristic1, heuristic1, heuristic1)


def get_heuristic_values_my_heuristic_rev(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2**nb_objects)
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    heuristic3 = nb_objects
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic2, heuristic1, -heuristic3)

def get_heuristic_values_my_heuristic_no_third(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2**nb_objects)
    heuristic2_numerator = 0
    heuristic2_denominator = 0
    for _, accuracy in examples_with_accuracies:
        heuristic2_numerator += accuracy
        heuristic2_denominator += 1
    if heuristic2_denominator != 0:
        heuristic2 = heuristic2_numerator / heuristic2_denominator
    else:
        heuristic2 = -inf
    return (heuristic1, heuristic2, heuristic2)


def get_random_heuristic_values_my_heuristic(nb_found_examples, examples_with_accuracies, nb_objects):
    return (random(), random(), random())

def get_most_objects_heuristic_values_my_heuristic(nb_found_examples, examples_with_accuracies, nb_objects):
    return (-nb_objects, -nb_objects, -nb_objects)

def get_heur1_and_most_objects_heuristic_values_my_heuristic(nb_found_examples, examples_with_accuracies, nb_objects):
    heuristic1 = nb_found_examples / (2 ** nb_objects)
    return (heuristic1, heuristic1, -nb_objects)


def get_examples_of_complex_relations_and_heuristic_values(complex_relation_name, rules, file_name, xml_output_directory, heuristic_function):
    object_id_to_object, all_objects = get_objects_id_to_objects_and_all_objects(file_name, xml_output_directory)
    if len(rules) == 0:
        complex_relation = Relation(complex_relation_name, 2, set())
        heuristic_value = heuristic_function(0, set(), len(all_objects))
        return complex_relation, heuristic_value
    base_relation_name_to_relation = get_base_relation_name_to_relation_dict(object_id_to_object)
    examples_with_accuracy = []
    complex_relation = Relation(complex_relation_name, rules[0].head.arity, set())
    for rule in rules:
        relation_name_to_relation = find_complex_rule_examples([rule], base_relation_name_to_relation, all_objects)
        # rule_accuracy = rule.nb_positive_train / (rule.nb_positive_train + rule.nb_negative_train)
        for _, relation in relation_name_to_relation.items():
            complex_relation.add_positive_examples(relation.positive_examples)

            for positive_example in relation.positive_examples:
                continue
                examples_with_accuracy.append((positive_example, rule_accuracy))
    # get heuristics
    heuristic_value = heuristic_function(len(complex_relation.positive_examples), examples_with_accuracy, len(all_objects))
    return complex_relation, heuristic_value


if __name__ == "__main__":
    xml_directory_path = "./xmls/"
    file_names = ["dummy_0", "dummy_1", "dummy_2", "dummy_3", "dummy_4", "dummy_5"]

    rules: list[Rule] = [Rule(Literal(False, "DirectlyFollows", 2, [0, 1]), [Literal(False, "ClosestUnderAndOverlap", 2, [1, 0])], 4, 0, 9.459824461736655, 4, 0), Rule(Literal(False, "DirectlyFollows", 2, [0, 1]), [Literal(False, "AtTipOfArrow", 2, [0, 2]), Literal(False, "AtBaseOfArrow", 2, [1, 2])], 5, 0, 11.82478057717082, 5, 0)]

    for rule in rules:
        print(rule)
    rule_head_name_to_rules = defaultdict(list)
    for rule in rules:
        head = rule.head
        rule_head_name_to_rules[head.name].append(rule)

    for rule_head_name, rules in rule_head_name_to_rules.items():
        print(f'\nComplex relation: {rule_head_name}')
        for file_name in file_names:
            xml_input_path = xml_directory_path + file_name + ".xml"
            object_id_to_object = get_objects_from_xml_file_path(xml_input_path)
            complex_relation, heuristic_values = get_examples_of_complex_relations_and_heuristic_values(rule_head_name, rules, file_name, xml_directory_path, get_heuristic_values_my_heuristic)
            print(f'found examples for file: {file_name}')
            print(complex_relation)
            print(f'{heuristic_values[0]=}')
            print(f'{heuristic_values[1]=}')
            print(f'{heuristic_values[2]=}')
            print()


