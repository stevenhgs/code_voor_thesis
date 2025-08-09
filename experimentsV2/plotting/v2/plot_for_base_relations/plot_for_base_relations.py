import os
import json
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18

# DirectlyFollows, Together
relation_name = "Together"

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

heuristic_names = [
    ("all", "alle basis-relaties"),
    ("positions_types_text", "posities + types + tekst"),
    ("positions_types", "posities + types"),
    ("only_positions", "posities"),
]
heuristics_points = dict()
for path_name, legend_name in heuristic_names:
    json_folder_path = f'../../../experiment4/results/{path_name}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            if file.split('.')[0] in ["BF3", "BF6"] and "Together":
                continue
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append(json.load(f))
    print(f'nb_files: {len(all_data)}')

    sum_f1_scores = [0 for _ in range(max_percentage + 1)]
    for percentage in range(max_percentage + 1):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            sum_f1_scores[percentage] += data["data"][f"{index}"]["scores"][relation_name]["f1_score"]
        sum_f1_scores[percentage] /= len(all_data)
    heuristics_points[(path_name, legend_name)] = sum_f1_scores


plt.ylim(0, 1.05)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=24)
plt.ylabel('Gemiddelde F1-score', fontsize=24)

"β={beam}, σ={significance}"

for path_name, legend_name in heuristic_names:
    plt.plot(x_points, heuristics_points[(path_name, legend_name)], label=f"{legend_name}")
plt.legend(loc="lower right", prop={'size': 15})
plt.show()
