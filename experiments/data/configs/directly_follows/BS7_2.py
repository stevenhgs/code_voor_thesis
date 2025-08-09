from src.custom_classes.Relation import Relation

config = {
    "BS7_2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2)}),
    },
"BS7_2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1)}),
    },
"BS7_2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1)}),
    },
"BS7_2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (4, 3), (6, 4), (7, 6)}),
    },
"BS7_2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (4, 3), (6, 4), (7, 6)}),
    },
"BS7_2_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(21, 19)}),
    },
"BS7_2_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5)}),
    },
"BS7_2_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
"BS7_2_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
"BS7_2_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4)}),
    },
}