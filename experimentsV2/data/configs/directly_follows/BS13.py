from src.custom_classes.Relation import Relation

config = {
    "BS13_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS13_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (13, 4), (8, 6), (9, 8)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (10, 9), (11, 9), (12, 9), (14, 13), (15, 13)}),
    },
"BS13_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)}),
"Together": Relation("Together", 2, {(5, 4), (6, 4), (8, 7)}),
    },
"BS13_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2)}),
"Together": Relation("Together", 2, {(3, 2), (5, 2), (4, 2), (7, 6), (8, 6), (9, 6)}),
    },
"BS13_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS13_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS13_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(3, 10), (4, 11), (5, 12), (6, 13), (7, 14)}),
    },
"BS13_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS13_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS13_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}