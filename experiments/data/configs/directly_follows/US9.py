from src.custom_classes.Relation import Relation

config = {
    "US9_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US9_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4)}),
    },
"US9_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6), (10, 7), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15), (17, 16)})
    },
"US9_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US9_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (2, 5), (6, 2), (7, 6), (8, 7), (10, 8), (11, 10), (12, 11), (16, 12), (13, 16), (14, 13), (15, 14)}),
    },
"US9_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2), (7, 6)}),
    },
"US9_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
    },
"US9_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (6, 4)}),
    },
"US9_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US9_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US9_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2)}),
    },
"US9_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}