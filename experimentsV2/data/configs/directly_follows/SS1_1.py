from src.custom_classes.Relation import Relation

config = {
    "SS1_1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (11, 8), (10, 11)}),
"Together": Relation("Together", 2, {(2, 1), (9, 11)}),
    },
"SS1_1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 1)}),
    },
"SS1_1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15)}),
"Together": Relation("Together", 2, {(17, 16), (18, 16), (19, 16), (20, 16), (21, 16), (22, 16), (23, 16)}),
    },
"SS1_1_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(6, 5), (8, 7)}),
    },
"SS1_1_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 2)}),
    },
"SS1_1_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (5, 2), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2)}),
    },
"SS1_1_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4), (7, 5), (9, 7)}),
"Together": Relation("Together", 2, {(2, 4), (6, 5), (8, 7), (10, 9), (11, 9)}),
    },
"SS1_1_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (7, 2), (8, 7), (3, 8), (4, 3), (5, 4), (6, 5), (9, 6), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13)}),
"Together": Relation("Together", 2, set()),
    },
"SS1_1_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (7, 5), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (6, 5), (10, 9)}),
    },
"SS1_1_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (7, 5), (8, 7), (10, 8), (11, 10)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (6, 5), (9, 8)}),
    },
"SS1_1_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (12, 9)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (6, 4), (13, 12), (10, 12), (11, 12), (7, 9), (8, 9)}),
    },
"SS1_1_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4)}),
    },
"SS1_1_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS1_1_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS1_1_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(2, 1), (8, 7)}),
    },
"SS1_1_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(2, 1), (6, 5)}),
    },
"SS1_1_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (7, 3), (5, 7), (6, 5), (8, 6), (10, 8)}),
"Together": Relation("Together", 2, {(2, 1), (4, 7), (9, 8), (11, 10)}),
    },
"SS1_1_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}