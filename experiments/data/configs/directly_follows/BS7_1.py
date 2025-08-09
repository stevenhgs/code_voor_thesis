from src.custom_classes.Relation import Relation

config = {
    "BS7_1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
"BS7_1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2)}),
    },
"BS7_1_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3)}),
    },
"BS7_1_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
    },
"BS7_1_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (6, 5)}),
    },
"BS7_1_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_1_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 9), (16, 12), (17, 16), (19, 17)}),
    },
"BS7_1_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3)}),
    },
"BS7_1_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(14, 11), (17, 14)}),
    },
"BS7_1_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_1_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_1_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
    },
}