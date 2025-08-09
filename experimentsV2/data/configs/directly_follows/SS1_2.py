from src.custom_classes.Relation import Relation

config = {
    "SS1_2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(0, 2), (1, 2)}),
    },
"SS1_2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (2, 6), (7, 2), (9, 7)}),
"Together": Relation("Together", 2, {(4, 3), (8, 7)}),
    },
"SS1_2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 8)}),
    },
"SS1_2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, {(4, 1), (5, 2), (6, 3)}),
    },
"SS1_2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"SS1_2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS1_2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (6, 4)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (7, 6), (8, 6)}),
    },
"SS1_2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (6, 3), (9, 6)}),
"Together": Relation("Together", 2, {(4, 3), (5, 3), (7, 6), (8, 9)}),
    },
"SS1_2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_2_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_2_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 5)}),
    },
"SS1_2_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (8, 5)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (7, 5)}),
    },
"SS1_2_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS1_2_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (14, 12), (16, 14)}),
"Together": Relation("Together", 2, {(19, 16), (18, 14), (3, 12), (4, 14), (5, 16), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2)}),
    },
"SS1_2_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 11), (11, 9)}),
"Together": Relation("Together", 2, {(0, 19), (1, 19), (2, 21), (3, 21), (4, 9), (5, 11), (6, 13), (7, 17), (8, 17), (16, 13), (15, 11)}),
    },
"SS1_2_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 11), (11, 9)}),
"Together": Relation("Together", 2, {(0, 19), (1, 19), (2, 21), (3, 21), (4, 9), (5, 11), (6, 13), (7, 17), (8, 17), (16, 13), (15, 11)}),
    },
"SS1_2_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 11), (11, 9)}),
"Together": Relation("Together", 2, {(0, 19), (1, 19), (2, 21), (3, 21), (4, 9), (5, 11), (6, 13), (7, 17), (8, 17), (16, 13), (15, 11)}),
    },
"SS1_2_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (9, 6), (10, 9), (11, 10)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (7, 5), (8, 6)}),
    },
"SS1_2_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS1_2_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS1_2_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (6, 4), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(5, 4), (11, 10)}),
    },
"SS1_2_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 9)}),
    },
"SS1_2_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (6, 5), (7, 6), (8, 7), (10, 8), (11, 10)}),
"Together": Relation("Together", 2, {(3, 2), (9, 8)}),
    },
"SS1_2_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (5, 2), (6, 5), (7, 6), (3, 7), (8, 3), (9, 8), (4, 9), (10, 4), (11, 10)}),
"Together": Relation("Together", 2, set()),
    },
}