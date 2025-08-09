import csv
from arrow_recognition import find_arrows_in_image

arrow_classes = ['36', '37', '38', '39', 'bullseye-arrow', 'arrow-bullseye', 'bullseye-arrow-bullseye']

positives = 0
negatives = 0
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
with open("./train/_annotations.csv") as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    count = 0
    for lines in csvFile:
        nb_arrows_found = find_arrows_in_image("./train/" + lines[0])
        print(f'arrows found: {nb_arrows_found}')
        if lines[3] in arrow_classes:
            positives += 1
            if nb_arrows_found > 0:
                true_positives += 1
            else:
                false_negatives += 1
        else:
            negatives += 1
            if nb_arrows_found > 0:
                false_positives += 1
            else:
                true_negatives += 1
        count += 1
        if count % 100 == 0:
            print(count)

    print(f'{negatives=}, {true_negatives=}, {false_positives=}')
    print(f'{positives=}, {true_positives=}, {false_negatives=}')
