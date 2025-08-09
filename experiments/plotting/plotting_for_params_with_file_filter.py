import os
import json
import matplotlib.pyplot as plt
from experiments.data.configs.directly_follows import BS0, BS1_short, BS2_short, BS3_short, BS4_short, BS5_short, BS6, BS7_1_short, BS7_2_short, BS8_short, BS9_short, BS10, BS11, BS12, BS13
from experiments.data.configs.directly_follows import SS1_1, SS1_2, SS2, SS3_1, SS3_2, SS3_3, SS3_4, SS4_1, SS4_2, SS4_3, SS5, SS6, SS7, SS8
from experiments.data.configs.directly_follows import US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12

combos = [
    (5, 0),
    (5, 10),
    (5, 20)
]

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

    sum_f1_scores = [0 for _ in range(101)]
    for percentage in range(101):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            sum_f1_scores[percentage] += data["data"][f"{index}"]["F1"]
        sum_f1_scores[percentage] /= len(all_data)
    points[(beam, significance)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, 100)
plt.xlabel('% geannoteerde slides')
plt.ylabel('Gemiddelde F1-score')

for beam, significance in combos:
    plt.plot(x_points, points[(beam, significance)], label=f"β={beam}, σ={significance}")
plt.legend(loc="lower right", prop={'size': 12})
plt.show()
