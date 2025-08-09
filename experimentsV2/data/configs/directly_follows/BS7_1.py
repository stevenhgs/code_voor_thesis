from src.custom_classes.Relation import Relation

config = {
    "BS7_1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2)}),
    },
"BS7_1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(3, 1), (2, 1), (4, 1), (5, 1)}),
    },
"BS7_1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(3, 5), (4, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6)}),
    },
"BS7_1_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 13), (2, 13), (3, 14), (4, 14), (5, 15), (6, 15), (7, 16), (8, 16), (10, 17), (11, 18), (12, 19)}),
    },
"BS7_1_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2)}),
"Together": Relation("Together", 2, {(4, 6), (5, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7)}),
    },
"BS7_1_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(5, 7), (6, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8)}),
    },
"BS7_1_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (6, 5), (8, 7), (9, 7), (14, 13), (15, 13)}),
    },
"BS7_1_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 10), (2, 11), (3, 12), (4, 13), (5, 14), (6, 15), (7, 16), (8, 17), (9, 17)}),
    },
"BS7_1_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 9), (16, 12), (17, 16), (19, 17)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4)}),
    },
"BS7_1_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(14, 11), (17, 14)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 10), (2, 10), (3, 10), (11, 10), (4, 8), (5, 8), (6, 8), (9, 8)}),
    },
"BS7_1_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"BS7_1_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, {(7, 6)}),
    },
}