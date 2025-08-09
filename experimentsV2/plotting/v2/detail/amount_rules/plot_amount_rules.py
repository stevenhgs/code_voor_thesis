import os
import json
import matplotlib.pyplot as plt
from experimentsV2.helpers.get_order_score import get_score, get_nb_rules

# DirectlyFollows, Together
combos = [
    (1, 3, False),
]

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


max_percentage = 50

x_points = [i for i in range(max_percentage + 1)]
points = dict()
for beam, significance, check_follows in combos:
    json_folder_path = f'../../../../experiment1/results/{beam}_{significance}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append(json.load(f))
    print(f'nb_files: {len(all_data)}')

    sum_f1_scores = [0 for _ in range(max_percentage + 1)]
    for percentage in range(max_percentage + 1):
        used_scores = 0
        used_slides = 0
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            nb_rules, used_to_add = get_nb_rules(data["data"], index, check_follows)
            sum_f1_scores[percentage] += nb_rules
            used_scores += used_to_add
        if used_scores > 0:
            sum_f1_scores[percentage] /= used_scores
        print(f'{used_scores=}')
    points[(beam, significance, check_follows)] = sum_f1_scores



plt.ylim(0, 6)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=16)
plt.ylabel('Gemiddelde aantal geleerde regels', fontsize=16)

"β={beam}, σ={significance}"
for beam, significance, check_follows in combos:
    plt.plot(x_points, points[(beam, significance, check_follows)], label=f"")
# plt.legend(loc="lower right", prop={'size': 12})
plt.show()