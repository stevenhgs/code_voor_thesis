import os
import json
import matplotlib.pyplot as plt
from experimentsV2.helpers.get_order_score import get_score
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 13
mpl.rcParams['ytick.labelsize'] = 13

check_follows = True
atleast_one_follows_to_use = False
combos = [
    (1, 3, atleast_one_follows_to_use),
]

def get_index_absolute(iteration, nb_pages):
    return min(iteration, nb_pages) + 1

nb_slides = 16
x_points = [i for i in range(nb_slides)]
points = dict()
for beam, significance, atleast_one_follows in combos:
    json_folder_path = f'../experiment1/results/{beam}_{significance}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append((json.load(f), file))


    sum_f1_scores = [0 for _ in range(nb_slides)]
    for percentage in range(nb_slides):
        used_scores = 0
        used_slides = 0
        for data, file in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index_absolute(percentage, nb_pages)
            print(index, file, nb_pages)
            while data["data"].get(f"{index}") is None:
                index -= 1
            f1_score_to_add, used_to_add, used_slides_to_add = get_score(data["data"], index, check_follows, atleast_one_follows)
            used_slides += used_slides_to_add
            sum_f1_scores[percentage] += f1_score_to_add
            used_scores += used_to_add
            if percentage == 80:
                print(percentage, data["data"][f"{index}"]["F1"])
        sum_f1_scores[percentage] /= len(all_data)
    points[(beam, significance)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, nb_slides - 1)
plt.xlabel('aantal geannoteerde slides', fontsize=16)
plt.ylabel('Gemiddelde F1-score', fontsize=16)

for beam, significance, atleast_one_follows in combos:
    plt.plot(x_points, points[(beam, significance)], label=f"β={beam}, σ={significance}")
# plt.legend(loc="lower right", prop={'size': 12})
plt.show()