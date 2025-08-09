from complete_pipeline.learn_rules import learn_rules_and_add_train_accuracy
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic, get_heuristic_values_my_heuristic_only_first
from complete_pipeline.configurations.access_control_config import config
from experimentsV2.helpers.learn_rulesV2 import learn_rules_and_add_train_accuracy_v2
from experimentsV2.helpers.get_order import get_order_score
from math import inf
from time import time
from collections import defaultdict
from src.pipeline.learn_rules_from_pdf_mfoil_context import learn_rules_from_pdf_in_context


def experiment_random(all_pdf_file_names, xml_path, config, heuristic_function, nb_iters=1, beam_size=10, min_significance=5):
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
    selected_slides = all_pdf_file_names[:5]
    complex_relation_names = ["DirectlyFollows", "Together"]


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
        reformed_config = dict()
        for key, relation_annotations in config.items():
            reformed_config[key] = {complex_relation_name: relation_annotations[complex_relation_name]}
        current_rules = learn_rules_from_pdf_in_context(selected_slides, xml_path, config, beam_size, min_significance)
        # filter rules
        filtered_rules = []
        for rule in current_rules:
            if rule.mfoil_significance >= min_significance:
                filtered_rules.append(rule)

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


        if nb_true_positives + nb_false_positives + nb_false_negatives == 0:
            f1_score = 1
            print(f'F1 score was 0')
        else:
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

    data[1] = {
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




if __name__ == "__main__":
    nb_of_xml_files = 35
    all_pdf_file_names = [f'access_control_{i}' for i in range(nb_of_xml_files)]
    xml_path = "./xmls/"
    config = config
    experiment(all_pdf_file_names, xml_path, config, get_heuristic_values_my_heuristic, nb_iters=len(all_pdf_file_names), beam_size=5, min_significance=0)
