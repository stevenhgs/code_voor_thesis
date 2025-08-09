import os
import json
import matplotlib.pyplot as plt

# DirectlyFollows, Together
relation_name = "DirectlyFollows"
combos = [
    (1, 3),
    (3, 3),
    (5, 3)
]

# 1. Path to your folder with JSON files
  # Adjust as needed

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
for beam, significance in combos:
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
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index(percentage, nb_pages)
            sum_f1_scores[percentage] += data["data"][f"{index}"]["scores"][relation_name]["f1_score"]
        sum_f1_scores[percentage] /= len(all_data)
    points[(beam, significance)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, max_percentage)
plt.xlabel('% geannoteerde slides', fontsize=16)
plt.ylabel('Gemiddelde F1-score', fontsize=16)

"β={beam}, σ={significance}"
for beam, significance in combos:
    plt.plot(x_points, points[(beam, significance)], label=f"β={beam}")
plt.legend(loc="lower right", prop={'size': 12})
plt.show()
