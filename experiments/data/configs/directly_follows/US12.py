from src.custom_classes.Relation import Relation

config = {
    "US12_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US12_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 9), (11, 10), (12, 11), (4, 2), (5, 4), (6, 5)}),
    },
"US12_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (3, 2), (4, 3)})
    },
"US12_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 9), (11, 10), (4, 2), (6, 4)}),
    },
"US12_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 5), (7, 6), (2, 1), (3, 2)}),
    },
"US12_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 10), (12, 11), (14, 13), (15, 14), (4, 2), (6, 4), (5, 3), (7, 5)}),
    },
"US12_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (3, 2), (4, 3)}),
    },
"US12_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US12_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (3, 2), (4, 3)}),
    },
"US12_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}