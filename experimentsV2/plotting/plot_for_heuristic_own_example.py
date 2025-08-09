import os
import json
import matplotlib.pyplot as plt

names = [
    ("my_heuristic_exp2", "methode"),
    ("only_first_exp2", "stap 1"),
    ("reversed_exp2", "stap 2, stap 1, stap 3"),
    ("random_exp3", "willekeurig"),
]

# 1. Path to your folder with JSON files
  # Adjust as needed

def get_index_absolute(iteration, nb_pages):
    return min(iteration, nb_pages) + 1




x_points = [i for i in range(42)]
points = dict()
for name, _ in names:
    json_folder_path = f'../experiment3/results/{name}'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append(json.load(f))


    sum_f1_scores = [0 for _ in range(42)]
    for percentage in range(42):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index_absolute(percentage, nb_pages)
            sum_f1_scores[percentage] += data["data"][f"{index}"]["F1"]
            if percentage == 80:
                print(percentage, data["data"][f"{index}"]["F1"])
        sum_f1_scores[percentage] /= len(all_data)
    points[(name)] = sum_f1_scores



plt.ylim(0, 1.05)
plt.xlim(0, 41)
plt.xlabel('Aantal geannoteerde slides')
plt.ylabel('Gemiddelde F1-score')

for name, legend_name in names:
    plt.plot(x_points, points[name], label=f"{legend_name}")
plt.legend(loc="lower right", prop={'size': 12})
plt.show()
