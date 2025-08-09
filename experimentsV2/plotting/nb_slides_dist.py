import os
import json
import matplotlib.pyplot as plt

# 1. Path to your folder with JSON files
json_folder_path = '../experiment4/results/all'  # Adjust as needed

# 2. Collect nb_pages_filtered values
nb_pages_filtered_values = [22, 33, 23]

for root, _, files in os.walk(json_folder_path):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    nb_pages_filtered = data['settings']['nb pages filtered']
                    nb_pages_filtered_values.append(nb_pages_filtered)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print(f'nb_files: {len(nb_pages_filtered_values)}')



# 3. Plot the histogram
min_val = min(nb_pages_filtered_values)
max_val = max(nb_pages_filtered_values)
bins = range(min_val - (min_val % 5), max_val + 5, 5)  # Bins in steps of 5

plt.figure(figsize=(10, 6))
plt.hist(nb_pages_filtered_values, bins=bins, edgecolor='black')
plt.ylim(top=16)
plt.xlabel('Aantal slides in een slide deck', fontsize=16)
plt.ylabel('Frequentie', fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
