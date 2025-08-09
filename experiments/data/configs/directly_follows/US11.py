from src.custom_classes.Relation import Relation

config = {
    "US11_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 9), (16, 12)}),
    },
"US11_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (8, 5), (9, 8), (10, 9)}),
    },
"US11_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set())
    },
"US11_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US11_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5), (8, 7), (9, 8), (10, 9)}),
    },
"US11_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US11_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 1), (9, 6), (13, 9)}),
    },
"US11_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US11_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US11_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (8, 3), (12, 8)}),
    },
"US11_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (9, 8)}),
    },
"US11_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (7, 5), (9, 7), (10, 9), (11, 10), (14, 11), (15, 14)}),
    },
"US11_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (9, 4), (12, 9), (15, 12)}),
    },
}