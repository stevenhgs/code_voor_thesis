import os
import traceback
import logging
from experiments.helpers.write_to_json import write_to_json
from experiments.helpers.experiment import experiment
from experiments.helpers.filter_max_objects import filter_max_objects
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic, get_random_heuristic_values_my_heuristic, get_heuristic_values_my_heuristic_rev, get_heuristic_values_my_heuristic_only_first, get_most_objects_heuristic_values_my_heuristic, get_heur1_and_most_objects_heuristic_values_my_heuristic, get_heuristic_values_my_heuristic_no_third, get_heuristic_values_step2, get_heuristic_values_step2_step1, get_heuristic_values_step2_step3
from experiments.data.configs.directly_follows import BS0, BS1_short, BS2_short, BS3_short, BS4_short, BS5_short, BS6, BS7_1_short, BS7_2_short, BS8_short, BS9_short, BS10, BS11, BS12, BS13
from experiments.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experiments.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12, exp
from experiments.data.configs.together import presentatie_verdediging_demo
from time import time

# redo: BS9_short, SS1_1, SS2, SS3_1, SS3_2, SS3_3

# name, config
input_data = [
    ("US1", US1.config),
("US2", US2.config),
("US3", US3.config),
("US4", US4.config),
("US5", US5.config),
("US6", US6.config),
("US7", US7.config),
("US8", US8.config),
("US9", US9.config),
("US10", US10.config),
("US11", US11.config),
("US12", US12.config),
]
input_data = [
    ("presentatie_verdediging_demo2", presentatie_verdediging_demo.config)
]

heuristics = [
    (get_heuristic_values_my_heuristic, "step2_step3"),
]

beam_size = 5
min_significance = 10
xml_path = './../data/xmls/'

if __name__ == "__main__":
    for heuristic, heuristic_name in heuristics:
        print(f'{beam_size=}, {min_significance}, {heuristic_name}')
        json_save_path = f'./results/etra/{heuristic_name}/'
        current_name = ""
        try:
            for name, config in input_data:
                current_name = name
                input_xml_path = xml_path + name + '/'
                nb_pages = len(os.listdir(input_xml_path)) - 1
                print(f'nb_pages: {nb_pages}')
                all_pdf_file_names = [f'{name}_{i}' for i in range(nb_pages)]
                filtered_names = filter_max_objects(all_pdf_file_names, input_xml_path, 39)
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

                results = experiment(
                                filtered_names,
                                input_xml_path,
                                config,
                                heuristic,
                                nb_iters=len(filtered_names), # NOTE: change accordingly
                                beam_size=beam_size,
                                min_significance=min_significance)

                data['data'] = results
                json_output_path = json_save_path + name + ".json"
                print(json_output_path)
                write_to_json(data, json_output_path)
        except Exception as e:
            print("Something went wrong: ", current_name)
            logging.error(traceback.format_exc())
