from src.custom_classes.Relation import Relation

config = {
    "BF5_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 7)}),
"Together": Relation("Together", 2, {(10, 11)}),
    },
"BF5_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(0, 4), (0, 2), (6, 4), (6, 2)}),
"Together": Relation("Together", 2, {(4, 5), (2, 3), (0, 1), (6, 7)}),
    },
"BF5_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BF5_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BF5_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 10), (8, 10), (8, 13), (7, 10), (7, 13), (11, 10), (11, 13), (11, 7)}),
"Together": Relation("Together", 2, {(13, 14), (11, 12), (8, 9)}),
    },
    "BF5_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "BF5_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 11), (7, 9)}),
"Together": Relation("Together", 2, {(11, 12), (9, 10), (7, 8)}),
    },
    "BF5_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(3, 4), (5, 6)}),
    },
"BF5_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(8, 6)}),
"Together": Relation("Together", 2, {(6, 7), (8, 9)}),
    },
"BF5_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 0)}),
"Together": Relation("Together", 2, {(0, 1), (2, 3), (4, 5)}),
    },
"BF5_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}