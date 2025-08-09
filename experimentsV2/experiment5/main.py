import os
import traceback
import logging
from experimentsV2.helpers.write_to_json import write_to_json
from experimentsV2.helpers.filter_max_objects import filter_max_objects
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic
from experimentsV2.data.configs.directly_follows import BS0, BS1, BS2, BS3, BS4_1, BS4_2, BS5, BS6_1, BS6_2, BS7_1, BS7_2, BS8, BS9, BS10, BS11, BS12, BS13
from experimentsV2.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experimentsV2.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12
from experimentsV2.data.configs.directly_follows import BF0, BF1, BF2, BF3, BF4_1, BF4_2, BF5, BF6
from time import time
import math
from complete_pipeline.learn_rules import learn_rules_and_add_train_accuracy
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic
from complete_pipeline.configurations.access_control_config import config
from experimentsV2.helpers.learn_rulesV2 import learn_rules_and_add_train_accuracy_v2
from experimentsV2.helpers.get_order import get_order_score
from math import inf
from time import time
from collections import defaultdict
from src.custom_classes.Rule import Rule
from src.custom_classes.Literal import Literal


def experiment_set_rules(all_pdf_file_names, xml_path, config, heuristic_function, nb_iters=1, beam_size=10, min_significance=5):
    """
    Assuming config only has 1 complex_relation.
    """
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    if nb_iters is None:
        nb_iters=len(all_pdf_file_names)
    data = dict()
    start = time()
    selected_slides = []
    complex_relation_names = ["DirectlyFollows", "Together"]

    relation_to_set_rules = {
        "DirectlyFollows": [
            Rule(Literal(False, "DirectlyFollows", 2, [0, 1]), [Literal(False, "XDimBefore", 2, [1, 0]), Literal(True, "Text", 1, [0])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "DirectlyFollows", 2, [0, 1]),[Literal(False, "YDimCovers", 2, [0, 1])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "DirectlyFollows", 2, [0, 1]),[Literal(False, "YDimEquals", 2, [0, 2]), Literal(False, "Text", 1, [1])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "DirectlyFollows", 2, [0, 1]),[Literal(False, "Text", 1, [0]), Literal(False, "YDimBefore", 2, [0, 1])], 1, 1, 1, 1, 1),
        ],
        "Together": [
            Rule(Literal(False, "Together", 2, [0, 1]),[Literal(False, "XDimBefore", 2, [1, 0]), Literal(True, "Text", 1, [0])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "Together", 2, [0, 1]), [Literal(False, "YDimCovers", 2, [0, 1])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "Together", 2, [0, 1]), [Literal(False, "YDimEquals", 2, [0, 2]),Literal(False, "Text", 1, [1])], 1, 1, 1, 1, 1),
            Rule(Literal(False, "Together", 2, [0, 1]), [Literal(False, "YDimBefore", 2, [0, 1]),Literal(True, "Text", 1, [0])], 1, 1, 1, 1, 1),
        ],
    }

    # iterations
    for iteration in range(nb_iters+1):
        if iteration % 5 == 0:
            print(f'{iteration}/{nb_iters}')
        # selection
        current_selected_slide = all_pdf_file_names[0]
        selected_heuristic_value = (inf, inf, 0)

        slide_to_heuristic_values = defaultdict(lambda : [0, 0, 0])
        slide_to_found_examples = defaultdict(lambda: {complex_relation_name: set() for complex_relation_name in complex_relation_names})
        slide_to_true_examples = defaultdict(lambda: {complex_relation_name: set() for complex_relation_name in complex_relation_names})

        relation_to_rules = defaultdict(list)
        relation_to_filtered_rules = defaultdict(list)
        # relation
        for complex_relation_name in complex_relation_names:
            print(f'{selected_slides=}')
            # metrics
            current_rules = relation_to_set_rules[complex_relation_name]
            filtered_rules = relation_to_set_rules[complex_relation_name]

            relation_to_rules[complex_relation_name] = [(str(rule), rule.mfoil_significance) for rule in current_rules]
            relation_to_filtered_rules[complex_relation_name] = [(str(rule), rule.mfoil_significance) for rule in filtered_rules]

            # slides
            for pdf_file_name in all_pdf_file_names:
                complex_relation, heuristic_value = get_examples_of_complex_relations_and_heuristic_values(complex_relation_name, filtered_rules, pdf_file_name, xml_path, heuristic_function)
                for i, value in enumerate(heuristic_value):
                    slide_to_heuristic_values[pdf_file_name][i] += value
                if complex_relation_name == complex_relation_names[-1]: # only check if both relations have been calculated
                    if pdf_file_name not in selected_slides:
                        if tuple(slide_to_heuristic_values[pdf_file_name]) < selected_heuristic_value:
                            current_selected_slide = pdf_file_name
                            selected_heuristic_value = tuple(slide_to_heuristic_values[pdf_file_name])
                found_examples = complex_relation.positive_examples
                slide_to_found_examples[pdf_file_name][complex_relation_name] = found_examples
                true_positives = config[pdf_file_name][complex_relation_name].positive_examples
                slide_to_true_examples[pdf_file_name][complex_relation_name] = true_positives


        relation_scores = dict()
        for complex_relation_name in complex_relation_names:
            scores = dict()
            nb_true_positives = 0
            nb_false_positives = 0
            nb_false_negatives = 0
            for pdf_file_name in all_pdf_file_names:
                found_examples = slide_to_found_examples[pdf_file_name][complex_relation_name]
                true_positives = slide_to_true_examples[pdf_file_name][complex_relation_name]
                for found_example in found_examples:
                    if found_example in true_positives:
                        nb_true_positives += 1
                    else:
                        # print(f'false positive: {pdf_file_name} {found_example=}')
                        nb_false_positives += 1
                for true_positive in true_positives:
                    if true_positive not in found_examples:
                        # print(f'false negative: {pdf_file_name} {true_positive=}')
                        nb_false_negatives += 1


            f1_score = (2 * nb_true_positives) / (2 * nb_true_positives + nb_false_positives + nb_false_negatives)
            print(f'{complex_relation_name} f1 score: {f1_score}')
            scores["nb_true_positives"] = nb_true_positives
            scores["nb_false_positives"] = nb_false_positives
            scores["nb_false_negatives"] = nb_false_negatives
            scores["f1_score"] = f1_score
            relation_scores[complex_relation_name] = scores

        pdf_name_to_order_data = dict()
        for pdf_file_name in all_pdf_file_names:
            pdf_name_to_order_data[pdf_file_name] = get_order_score(slide_to_found_examples[pdf_file_name], slide_to_true_examples[pdf_file_name], pdf_file_name, xml_path)


        # print(f'\t{BOLD + UNDERLINE}F1 score:{END + END} {f1_score}')
        end = time()
        print(f'time taken: {int(end - start)}s')

        selected_slides.append(current_selected_slide)
        data[iteration+1] = {
            "scores": relation_scores,
            "time": end - start,
            "selected slide": selected_slides[-1],
            "selected slides:": list(selected_slides),
            "selected heuristic value": selected_heuristic_value,
            "rules": relation_to_rules,
            "filtered rules": relation_to_filtered_rules,
            "order_data": pdf_name_to_order_data,
        }

    return data


# name, config
input_data = [
    ("BF0", BF0.config),
    ("BF1", BF1.config),
    ("BF2", BF2.config),
    ("BF4_1", BF4_1.config),
    ("BF4_2", BF4_2.config),
    ("BF5", BF5.config),
    ("BF6", BF6.config),
]


beam_sizes = [1]
min_significances = [3]
xml_path = './../data/xmls/'

def get_all_names(input_xml_path):
    all_names = os.listdir(input_xml_path)
    underscore_count1 = all_names[0].count('_')
    underscore_count2 = all_names[1].count('_')
    underscore_count3 = all_names[2].count('_')
    underscore_count_to_use = underscore_count2
    if underscore_count1 == underscore_count2:
        underscore_count_to_use = underscore_count2
    if underscore_count1 == underscore_count3:
        underscore_count_to_use = underscore_count3
    if underscore_count2 == underscore_count3:
        underscore_count_to_use = underscore_count2
    output = []
    for name in all_names:
        if name.count('_') == underscore_count_to_use:
            output.append(name.split('.')[0])
    return output

if __name__ == "__main__":
    for beam_size in beam_sizes:
        for min_significance in min_significances:
            print(f'{beam_size=}, {min_significance}')
            json_save_path = f'./results/new/'
            current_name = ""

            for name, config in input_data:
                try:
                    current_name = name
                    input_xml_path = xml_path + name + '/'
                    all_pdf_file_names = get_all_names(input_xml_path)
                    nb_pages = len(all_pdf_file_names)
                    print(f'nb_pages: {nb_pages}')
                    filtered_names = filter_max_objects(all_pdf_file_names, input_xml_path, 25)
                    print("filtered_names:")
                    print(filtered_names)
                    data = {"settings": {
                        "beam size": beam_size,
                        "min significance": min_significance,
                        "nb pages": nb_pages,
                        "all pdf names": all_pdf_file_names,
                        "nb pages filtered": len(filtered_names),
                        "all filtered names": filtered_names
                    }}
                    nb_iters = math.ceil(len(filtered_names) * 0.7)
                    print(f'{len(filtered_names)} --> {nb_iters} ')
                    results = experiment_set_rules(
                                    filtered_names,
                                    input_xml_path,
                                    config,
                                    get_heuristic_values_my_heuristic,
                                    nb_iters=1, # NOTE: change accordingly
                                    beam_size=beam_size,
                                    min_significance=min_significance)

                    data['data'] = results
                    json_output_path = json_save_path + name + ".json"
                    print(json_output_path)
                    write_to_json(data, json_output_path)
                except Exception as e:
                    print("Something went wrong: ", current_name)
                    logging.error(traceback.format_exc())
