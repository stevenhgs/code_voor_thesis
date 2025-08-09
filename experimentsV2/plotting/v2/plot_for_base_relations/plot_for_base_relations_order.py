import os
import json
import matplotlib.pyplot as plt
from experimentsV2.helpers.get_order_score import get_score
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18

check_follows = True
atleast_one_follows_to_use = False
beta = 1
combos = [
    (beta, 3, atleast_one_follows_to_use),
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


max_percentage = 30

x_points = [i for i in range(max_percentage + 1)]

points_heuristic = dict()
heuristic_names = [
    ("all", "alle basis-relaties", atleast_one_follows_to_use),
    ("positions_types_text", "posities + types + tekst", atleast_one_follows_to_use),
    ("positions_types", "posities + types", atleast_one_follows_to_use),
    ("only_positions", "posities", atleast_one_follows_to_use),
]
for path_name, legend_name, atleast_one_follows in heuristic_names:
    json_folder_path = f'../../../experiment4/results/{path_name}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
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
    points_heuristic[(path_name, legend_name, atleast_one_follows)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=24)
plt.ylabel('Gemiddelde F1-score', fontsize=24)

"β={beam}, σ={significance}"

for path_name, legend_name, atleast_one_follows in heuristic_names:
    plt.plot(x_points, points_heuristic[(path_name, legend_name, atleast_one_follows)], label=f"{legend_name}")
plt.legend(loc="lower right", prop={'size': 15})
plt.show()
