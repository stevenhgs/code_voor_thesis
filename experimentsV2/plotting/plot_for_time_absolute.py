import os
import json
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 13
mpl.rcParams['ytick.labelsize'] = 13

relation_name = "Together"
names = [
    (1, 3),
    (3, 3),
    (5, 3),
]

def get_index_absolute(iteration, nb_pages):
    return min(iteration, nb_pages) + 1

nb_slides = 16
x_points = [i for i in range(nb_slides+1)]
points = dict()
for beam, significance in names:
    json_folder_path = f'../experiment2/results/something'
    all_data = []
    for root, _, files in os.walk(json_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                all_data.append(json.load(f))


    sum_f1_scores = [0 for _ in range(nb_slides + 1)]
    for percentage in range(nb_slides + 1):
        for data in all_data:
            nb_pages = data["settings"]["nb pages filtered"]
            index = get_index_absolute(percentage, nb_pages)
            while data["data"].get(str(index)) is None:
                index -= 1
            sum_f1_scores[percentage] += data["data"][f"{index}"]["time"]
        sum_f1_scores[percentage] /= len(all_data)
    points[(beam, significance)] = sum_f1_scores

max_time = max([e[-1] for _, e in points.items()])


plt.ylim(0, max_time * 1.1)
plt.xlim(0, nb_slides)
plt.xlabel('% geannoteerde slides', fontsize=20)
plt.ylabel('verlopen tijd in seconden', fontsize=20)

for beam, significance in names:
    plt.plot(x_points, points[(beam, significance)], label=f"β={beam}")
plt.legend(loc='lower right',
          fancybox=True, ncol=1, prop={'size': 12})
plt.show()