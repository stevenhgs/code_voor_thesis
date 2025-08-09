from experimentsV2.data.configs.directly_follows import BS0, BS1, BS2, BS3, BS4_1, BS4_2, BS5, BS6_1, BS6_2, BS7_1, BS7_2, BS8, BS9, BS10, BS11, BS12, BS13
from experimentsV2.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experimentsV2.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12
from experimentsV2.data.configs.directly_follows import BF0, BF1, BF2, BF3, BF4_1, BF4_2, BF5, BF6
import os
import json


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

all_names = [e[0] for e in input_data]

beam = 1
significance = 6

json_folder_path = f'../experiment1/results/{beam}_{significance}'
found_names = set()
for root, _, files in os.walk(json_folder_path):
    for file in files:
        file_name = file.split('.')[0]
        found_names.add(file_name)

for name in all_names:
    if name not in found_names:
        print(name)