import os
import json
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
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
heuristic_names = [
    ("all", "alle basis-relaties"),
    ("positions_types_text", "posities + types + tekst"),
    ("positions_types", "posities + types"),
    ("only_positions", "posities"),
]

x_points = [i for i in range(max_percentage + 1)]
points = dict()
for path_name, legend_name in heuristic_names:
    json_folder_path = f'../../../experiment4/results/{path_name}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append(json.load(f))


    sum_f1_scores = [0 for _ in range(max_percentage + 1)]
    for percentage in range(max_percentage + 1):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            sum_f1_scores[percentage] += data["data"][f"{index}"]["time"]
        sum_f1_scores[percentage] /= len(all_data)
    points[(path_name, legend_name)] = sum_f1_scores

max_time = max([e[-1] for _, e in points.items()])


plt.ylim(0, max_time * 1.1)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=20)
plt.ylabel('verlopen tijd in seconden', fontsize=20)

for path_name, legend_name in heuristic_names:
    plt.plot(x_points, points[(path_name, legend_name)], label=f"{legend_name}")
plt.legend(loc='upper left',
          fancybox=True, ncol=1, prop={'size': 14})
plt.show()
