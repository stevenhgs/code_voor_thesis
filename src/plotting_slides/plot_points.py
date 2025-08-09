import matplotlib.pyplot as plt

text = '''<curve linewidth="0" bbox="195.940,248.330,272.570,310.410" pts="198.760,310.410,265.200,257.120,262.390,253.610,195.940,306.900,266.260,262.040,272.570,248.330,257.820,251.510"/>'''

split_lines = text.split('<')[1:]
split_by_points = [e.split("pts=")[1][1:-4] for e in split_lines]

coords = [[], []]
print(coords)

for i, line in enumerate(split_by_points):
    if i % 3 != 2:
        continue
    split_by_comma = line.split(',')
    for j in range(len(split_by_comma)):
        coords[j % 2].append(float(split_by_comma[j]))


for i in range(0, len(coords[0]), 1):
    plt.plot(coords[0][i:i+2], coords[1][i:i+2], 'ro-')
plt.show()
