from complete_pipeline.learn_rules import learn_rules_and_add_train_accuracy
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic
from complete_pipeline.configurations.dummy_configuration import config
from complete_pipeline.configurations.access_control_config import config
from math import inf
from time import time


def experiment(all_pdf_file_names, xml_path, config, heuristic_function, nb_iters=None, beam_size=10, min_significance=5):
    """
    Assuming config only has 1 complex_relation.
    """
    if nb_iters is None:
        nb_iters=len(all_pdf_file_names)
    data = dict()
    start = time()
    selected_slides = []
    complex_relation_name = None
    for pdf_name, relation_name_to_relation_dict in config.items():
        for relation_name, _ in relation_name_to_relation_dict.items():
            complex_relation_name = relation_name
    for iteration in range(nb_iters+1):
        # selection
        current_selected_slide = all_pdf_file_names[0]
        selected_heuristic_value = (inf, inf, 0)
        # metrics
        nb_true_positives = 0
        nb_false_positives = 0
        nb_false_negatives = 0
        current_rules = learn_rules_and_add_train_accuracy(selected_slides, xml_path, config, beam_size, min_significance=min_significance)
        # filter rules
        filtered_rules = []
        for rule in current_rules:
            if rule.mfoil_significance >= min_significance:
                filtered_rules.append(rule)
        current_rules = filtered_rules
        print("getting examples...")
        for pdf_file_name in all_pdf_file_names:
            complex_relation, heuristic_value = get_examples_of_complex_relations_and_heuristic_values(complex_relation_name, current_rules, pdf_file_name, xml_path, heuristic_function)
            if pdf_file_name not in selected_slides:
                if heuristic_value < selected_heuristic_value:
                    current_selected_slide = pdf_file_name
                    selected_heuristic_value = heuristic_value
            found_examples = complex_relation.positive_examples
            true_positives = config[pdf_file_name][complex_relation_name].positive_examples
            for found_example in found_examples:
                if found_example in true_positives:
                    nb_true_positives += 1
                else:
                    print(f'false positive: {pdf_file_name} {found_example=}')
                    nb_false_positives += 1
            for true_positive in true_positives:
                if true_positive not in found_examples:
                    print(f'false negative: {pdf_file_name} {true_positive=}')
                    nb_false_negatives += 1
        print("found examples")

        print(f'{BOLD + UNDERLINE}iteration{END + END}: {iteration}')
        print(f'{BOLD + UNDERLINE}current selected slides{END + END}: {selected_slides}')
        print(f'{BOLD + UNDERLINE}current_rules{END + END}:')
        for rule in current_rules:
            print("\t" + str(rule), f'significance: {rule.mfoil_significance}')
        print(f'{BOLD + UNDERLINE}selected slide{END + END}: {current_selected_slide}')
        print(f'{BOLD + UNDERLINE}metrics:{END + END}')
        print(f'\t{BOLD + UNDERLINE}True positives:{END + END} {nb_true_positives}')
        print(f'\t{BOLD + UNDERLINE}False positives:{END + END} {nb_false_positives}')
        print(f'\t{BOLD + UNDERLINE}False negatives:{END + END} {nb_false_negatives}')
        f1_score = (2 * nb_true_positives) / (2 * nb_true_positives + nb_false_positives + nb_false_negatives)
        print(f'\t{BOLD + UNDERLINE}F1 score:{END + END} {f1_score}')
        end = time()
        print(f'time taken: {end - start}s')
        print(f'\n\n')
        selected_slides.append(current_selected_slide)
        data[iteration+1] = {
            "TP": nb_true_positives,
            "FP": nb_false_negatives,
            "FN": nb_false_negatives,
            "F1": f1_score,
            "time": end - start,
            "selected slide": selected_slides[-1],
            "selected heuristic value": selected_heuristic_value,
            "rules": [(str(rule), rule.mfoil_significance) for rule in current_rules],
        }

    return data




if __name__ == "__main__":
    # Note: change config at the top as well!
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    nb_of_xml_files = 35
    all_pdf_file_names = [f'access_control_{i}' for i in range(nb_of_xml_files)]
    xml_path = "./xmls/"
    config = config
    experiment(all_pdf_file_names, xml_path, config, get_heuristic_values_my_heuristic, nb_iters=len(all_pdf_file_names), beam_size=5, min_significance=0)
