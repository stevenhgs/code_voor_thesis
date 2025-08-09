from src.custom_classes.Relation import Relation

config = {
    "BS12_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS12_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS12_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS12_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 10), (12, 11), (13, 12)}),
"Together": Relation("Together", 2,  {(2, 15), (3, 16), (4, 18), (5, 19), (6, 20), (13, 12), (14, 12)}),
    },
"BS12_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS12_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS12_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (7, 14), (8, 15), (9, 16), (10, 17), (11, 18), (12, 19)}),
    },
"BS12_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS12_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (8, 7), (9, 7), (10, 7)}),
    },
"BS12_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS12_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (7, 4)}),
"Together": Relation("Together", 2, {(5, 3), (6, 4), (8, 7), (9, 7)}),
    },
"BS12_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (6, 4), (9, 6), (10, 9), (11, 10)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (8, 6), (12, 11)}),
    },
"BS12_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS12_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 5), (2, 1), (3, 2), (4, 3), (7, 4)}),
"Together": Relation("Together", 2, {(6, 5), (8, 7)}),
    },
"BS12_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}