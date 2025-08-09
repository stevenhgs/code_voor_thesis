import os
import traceback
import logging
from experimentsV2.helpers.write_to_json import write_to_json
from experimentsV2.helpers.experiment import experiment_v2
from experimentsV2.helpers.filter_max_objects import filter_max_objects
from complete_pipeline.apply_rules import get_examples_of_complex_relations_and_heuristic_values, get_heuristic_values_my_heuristic
from experimentsV2.data.configs.directly_follows import BS0, BS1, BS2, BS3, BS4_1, BS4_2, BS5, BS6_1, BS6_2, BS7_1, BS7_2, BS8, BS9, BS10, BS11, BS12, BS13
from experimentsV2.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experimentsV2.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12
from experimentsV2.data.configs.directly_follows import BF0, BF1, BF2, BF3, BF4_1, BF4_2, BF5, BF6
from time import time
import math


# name, config
input_data = [
    ("BF2", BF2.config),
]


beam_sizes = [5]
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
            json_save_path = f'./results/{beam_size}_{min_significance}/'
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
                    results = experiment_v2(
                                    filtered_names,
                                    input_xml_path,
                                    config,
                                    get_heuristic_values_my_heuristic,
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
