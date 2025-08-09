import os
import traceback
import logging
from experimentsV2.helpers.write_to_json import write_to_json
from experimentsV2.helpers.experiment import experiment_v2
from experimentsV2.helpers.filter_max_objects import filter_max_objects
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic, get_heuristic_values_step2, get_heuristic_values_my_heuristic_only_first, get_random_heuristic_values_my_heuristic, get_most_objects_heuristic_values_my_heuristic
from experimentsV2.data.configs.directly_follows import BS0, BS1, BS2, BS3, BS4_1, BS4_2, BS5, BS6_1, BS6_2, BS7_1, BS7_2, BS8, BS9, BS10, BS11, BS12, BS13
from experimentsV2.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experimentsV2.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12
from experimentsV2.data.configs.directly_follows import BF0, BF1, BF2, BF3, BF4_1, BF4_2, BF5, BF6
from time import time
import math
from experimentsV2.helpers.experiment_random import experiment_random


# name, config
input_data = [
    ("BF0", BF0.config),
("BF1", BF1.config),
("BF2", BF2.config),
("BF3", BF3.config),
("BF4_1", BF4_1.config),
("BF4_2", BF4_2.config),
("BF5", BF5.config),
("BF6", BF6.config),
("BS0", BS0.config),
("BS1", BS1.config),
("BS2", BS2.config),
("BS3", BS3.config),
("BS4_1", BS4_1.config),
("BS4_2", BS4_2.config),
("BS5", BS5.config),
("BS6_1", BS6_1.config),
("BS6_2", BS6_2.config),
("BS7_1", BS7_1.config),
("BS7_2", BS7_2.config),
("BS8", BS8.config),
("BS9", BS9.config),
("BS10", BS10.config),
("BS11", BS11.config),
("BS12", BS12.config),
("BS13", BS13.config),
("SS1_1", SS1_1.config),
("SS1_2", SS1_2.config),
("SS2", SS2.config),
("SS3_1", SS3_1.config),
("SS3_3", SS3_3.config),
("SS3_4", SS3_4.config),
("SS4_1", SS4_1.config),
("SS4_2", SS4_2.config),
("SS4_3", SS4_3.config),
("SS5", SS5.config),
("SS6", SS6.config),
("SS8", SS8.config),
("US1", US1.config),
("US2", US2.config),
("US3", US3.config),
("US4", US4.config),
("US5", US5.config),
("US6", US6.config),
("US7", US7.config),
("US8", US8.config),
("US9", US9.config),
("US11", US11.config),
("US12", US12.config),
]

heuristics = [
    (get_heuristic_values_step2, "something"),
]

# NOTE: set!
beam_size = 1
min_significance = 3
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
    for heuristic, heuristic_name in heuristics:
        print(f'{beam_size=}, {min_significance}')
        json_save_path = f'./results/{heuristic_name}/'
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
                results = experiment_random(
                                filtered_names,
                                input_xml_path,
                                config,
                                heuristic,
                                nb_iters=nb_iters, # NOTE: change accordingly
                                beam_size=beam_size,
                                min_significance=min_significance)

                data['data'] = results
                json_output_path = json_save_path + name + ".json"
                print(json_output_path)
                write_to_json(data, json_output_path)
            except Exception as e:
                print("Something went wrong: ", current_name)
                logging.error(traceback.format_exc())
