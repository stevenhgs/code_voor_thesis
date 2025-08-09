from src.custom_classes.Relation import Relation

config = {
    "US10_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US10_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7)}),
    },
"US10_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (6, 5), (7, 6), (8, 7), (9, 8)})
    },
"US10_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (6, 3), (8, 6)}),
    },
"US10_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13)}),
    },
"US10_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 3)}),
    },
"US10_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 3)}),
    },
"US10_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US10_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 8), (12, 8), (10, 8)}),
    },
"US10_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2)}),
    },
"US10_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2)}),
    },
"US10_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (13, 12), (15, 12), (14, 12)}),
    },
"US10_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (6, 5)}),
    },
"US10_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (7, 3), (9, 7)}),
    },
"US10_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (7, 4)}),
    },
"US10_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4), (6, 5), (7, 6), (10, 7), (12, 10)}),
    },
"US10_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US10_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US10_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2)}),
    },
"US10_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
    },
"US10_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4), (7, 5), (8, 7), (10, 8), (11, 10), (12, 11), (13, 12)}),
    },
"US10_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (7, 5), (8, 7), (9, 8), (10, 9)}),
    },
"US10_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (7, 5), (8, 7)}),
    },
"US10_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}