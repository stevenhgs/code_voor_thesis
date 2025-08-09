from src.custom_classes.Relation import Relation

config = {
    "US12_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US12_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 9), (11, 10), (12, 11)}),
"Together": Relation("Together", 2, {(2, 9), (4, 10), (5, 11), (6, 12), (3, 2), (7, 6)}),
    },
"US12_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(2, 6), (3, 7), (4, 8)}),
    },
"US12_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 9), (11, 10)}),
"Together": Relation("Together", 2, {(2, 9), (3, 2), (4, 10), (5, 4), (6, 11), (7, 6)}),
    },
"US12_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 5), (7, 6), (2, 1), (3, 2)}),
"Together": Relation("Together", 2, {(1, 5), (2, 6), (3, 7)}),
    },
"US12_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 10), (12, 11), (14, 13), (15, 14)}),
"Together": Relation("Together", 2, {(2, 10), (4, 11), (6, 12), (3, 13), (5, 14), (7, 15)}),
    },
"US12_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(2, 6), (3, 7), (4, 8)}),
    },
"US12_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US12_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(2, 6), (3, 7), (4, 8)}),
    },
"US12_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}