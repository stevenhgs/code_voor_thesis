from src.custom_classes.Relation import Relation

config = {
    "US5_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US5_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4), (7, 6), (8, 7), (9, 8), (11, 9)}),
    },
"US5_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (8, 5), (9, 8), (11, 9), (12, 11), (14, 12)})
    },
"US5_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (9, 3), (11, 9)}),
    },
"US5_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (8, 6), (10, 8), (11, 10), (14, 11)}),
    },
"US5_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (8, 6), (9, 8), (10, 9), (11, 10), (12, 11)}),
    },
"US5_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (7, 5), (10, 7), (13, 10), (15, 13), (16, 15), (17, 16), (19, 17), (22, 19)}),
    },
"US5_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (6, 5), (7, 6), (10, 7), (11, 10), (12, 11)}),
    },
"US5_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (7, 5), (8, 7), (9, 8), (11, 9)}),
    },
"US5_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (2, 10), (13, 2), (14, 13), (15, 14), (16, 15), (17, 16)}),
    },
"US5_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US5_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US5_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US5_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2), (10, 6), (11, 10), (12, 11), (14, 12)}),
    },
"US5_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US5_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 2), (4, 1), (6, 4), (5, 6), (7, 5), (8, 7), (9, 8), (11, 9), (12, 11)}),
    },
}