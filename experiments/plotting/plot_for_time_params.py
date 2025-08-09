import os
import json
import matplotlib.pyplot as plt
from experiments.data.configs.directly_follows import BS0, BS1_short, BS2_short, BS3_short, BS4_short, BS5_short, BS6, BS7_1_short, BS7_2_short, BS8_short, BS9_short, BS10, BS11, BS12, BS13
from experiments.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experiments.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12

combos = [
    (1, 10),
    (3, 10),
    (5, 10)
]

input_data = [
    ("BS0", BS0.config),
    ("BS1_short", BS1_short.config),
    ("BS2_short", BS2_short.config),
    ("BS3_short", BS3_short.config),
    ("BS4_short", BS4_short.config),
    ("BS5_short", BS5_short.config),
    ("BS6", BS6.config),
    ("BS7_1_short", BS7_1_short.config),
    ("BS7_2_short", BS7_2_short.config),
    ("BS8_short", BS8_short.config),
    ("BS9_short", BS9_short.config),
    ("BS10", BS10.config),
    ("BS11", BS11.config),
    ("BS12", BS12.config),
    ("BS13", BS13.config),
    ("SS1_1", SS1_1.config),
    ("SS1_2", SS1_2.config),
    ("SS2", SS2.config),
    ("SS3_1", SS3_1.config),
    ("SS3_2", SS3_2.config),
    ("SS3_3", SS3_3.config),
    ("SS3_4", SS3_4.config),
    ("SS4_1", SS4_1.config),
    ("SS4_2", SS4_2.config),
    ("SS4_3", SS4_3.config),
    ("SS5", SS5.config),
    ("SS6", SS6.config),
    ("SS7", SS7.config),
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
    ("US10", US10.config),
    ("US11", US11.config),
    ("US12", US12.config),
]

allowed_files = [e[0] + ".json" for e in input_data]

# 1. Path to your folder with JSON files
  # Adjust as needed

def get_index(percentage, nb_pages):
    """
    assume 37 pages
    perc -> index
    0 -> 0
    1 -> 0
    2 -> 0
    3 -> 1
    100 -> 37
    """
    return int((percentage * nb_pages) // 100) + 1




x_points = [i for i in range(101)]
points = dict()
for beam, significance in combos:
    json_folder_path = f'../experiment1/results/{beam}_{significance}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            if file in allowed_files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    all_data.append(json.load(f))
    print(f'nb_files: {len(all_data)}')

    sum_time_scores = [0 for _ in range(101)]
    for percentage in range(101):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            sum_time_scores[percentage] += data["data"][f"{index}"]["time"]
        sum_time_scores[percentage] /= len(all_data)
    points[(beam, significance)] = sum_time_scores

max_time = 0
for beam, significance in combos:
    max_time = max(max_time, max(points[(beam, significance)]))

plt.ylim(0, max_time * 1.1)
plt.xlim(0, 100)
plt.xlabel('% geannoteerde slides')
plt.ylabel('Gemiddelde verrstreken tijd in seconden')

for beam, significance in combos:
    plt.plot(x_points, points[(beam, significance)], label=f"β={beam}, σ={significance}")
plt.legend(loc="lower right", prop={'size': 12})
plt.show()
