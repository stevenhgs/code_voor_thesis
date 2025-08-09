import os
import json
import matplotlib.pyplot as plt
from experimentsV2.helpers.get_order_score import get_score

check_follows = True
atleast_one_follows_to_use = False
sigma = 0
combos = [
    (1, sigma, atleast_one_follows_to_use),
    (3, sigma, atleast_one_follows_to_use),
    (5, sigma, atleast_one_follows_to_use),
]

allowed_file_names = {
    "BF0",
"BF1",
"BF2",
"BF3",
"BF4_1",
"BF4_2",
"BF5",
"US12"
}

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
for beam, significance, atleast_one_follows in combos:
    json_folder_path = f'../../../experiment1/results/{beam}_{significance}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            if file.split('.')[0] not in allowed_file_names:
                continue
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
            f1_score_to_add, used_to_add, used_slides_to_add = get_score(data["data"], index, check_follows, atleast_one_follows)
            used_slides += used_slides_to_add
            sum_f1_scores[percentage] += f1_score_to_add
            used_scores += used_to_add
        if used_scores > 0:
            sum_f1_scores[percentage] /= used_scores
        print(f'{used_scores=} {used_slides=}')
    points[(beam, significance, atleast_one_follows)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=16)
plt.ylabel('Gemiddelde F1-score', fontsize=16)

"β={beam}, σ={significance}"
for beam, significance, atleast_one_follows in combos:
    plt.plot(x_points, points[(beam, significance, atleast_one_follows)], label=f"β={beam}")
plt.legend(loc="lower right", prop={'size': 12})
plt.show()
