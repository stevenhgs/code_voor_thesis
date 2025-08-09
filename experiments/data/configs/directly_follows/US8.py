from src.custom_classes.Relation import Relation

config = {
    "US8_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4), (8, 6), (9, 8), (10, 9)}),
    },
"US8_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (13, 11)})
    },
"US8_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (9, 7)}),
    },
"US8_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (5, 4), (7, 5)}),
    },
"US8_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (5, 4), (6, 5), (7, 6)}),
    },
"US8_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
"US8_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US8_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (8, 5), (10, 8)}),
    },
}