from src.custom_classes.Relation import Relation

config = {
    "SS8_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, set()),
    },
"SS8_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS8_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (6, 4), (8, 6), (9, 8), (10, 9), (11, 10)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (7, 6)}),
    },
"SS8_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (8, 5), (9, 8), (11, 9)}),
"Together": Relation("Together", 2, {(7, 2), (4, 3), (6, 5), (10, 9)}),
    },
"SS8_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, set()),
    },
"SS8_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5), (6, 7), (8, 6)}),
"Together": Relation("Together", 2, set()),
    },
"SS8_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS8_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}