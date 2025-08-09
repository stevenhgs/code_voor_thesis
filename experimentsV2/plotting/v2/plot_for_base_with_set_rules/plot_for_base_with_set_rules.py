import os
import json
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 13
mpl.rcParams['ytick.labelsize'] = 13

relation_name = "Together"
combos = [
    (1, 3)
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


points_base = dict()
for beam, significance in combos:
    json_folder_path = f'../../../experiment5/results/new'
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
            sum_f1_scores[percentage] += data["data"][f"{2}"]["scores"][relation_name]["f1_score"]
        sum_f1_scores[percentage] /= len(all_data)
    points_base[(beam, significance)] = sum_f1_scores




plt.ylim(0, 1.05)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=16)
plt.ylabel('Gemiddelde F1-score', fontsize=16)

"β={beam}, σ={significance}"

for beam, significance in combos:
    plt.plot(x_points, points_base[(beam, significance)], '--', label=f"vaste regels")

plt.legend(loc="lower right", prop={'size': 12})
plt.show()
