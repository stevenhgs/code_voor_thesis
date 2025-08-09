from src.custom_classes.Relation import Relation

config = {
    "US10_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(0, 5), (1, 5)}),
    },
"US10_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(9, 6), (10, 7), (11, 8), (0, 12)}),
    },
"US10_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(0, 12), (10, 9), (11, 9)}),
    },
"US10_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (6, 3), (8, 6)}),
"Together": Relation("Together", 2, {(0, 9), (2, 1), (4, 3), (5, 3), (7, 6)}),
    },
"US10_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13)}),
"Together": Relation("Together", 2, {(0, 15)}),
    },
"US10_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 3)}),
"Together": Relation("Together", 2, {(2, 11), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (10, 9)}),
    },
"US10_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 3)}),
"Together": Relation("Together", 2, {(0, 2), (4, 3), (5, 3)}),
    },
"US10_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(8, 0)}),
    },
"US10_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 8), (12, 8), (10, 8)}),
"Together": Relation("Together", 2, {(7, 0), (2, 1), (13, 8), (12, 8), (10, 8)}),
    },
"US10_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (0, 8), (1, 8)}),
    },
"US10_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2)}),
"Together": Relation("Together", 2, {(0, 12), (3, 2), (4, 2), (5, 2), (7, 6), (8, 6), (9, 6)}),
    },
"US10_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (13, 12), (15, 12), (14, 12)}),
"Together": Relation("Together", 2, {(0, 11), (3, 2), (5, 4), (6, 4), (8, 7), (13, 12), (15, 12), (14, 12)}),
    },
"US10_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (6, 5)}),
"Together": Relation("Together", 2, {(0, 11), (1, 11), (3, 2), (4, 2), (7, 6), (8, 6), (9, 6), (10, 6)}),
    },
"US10_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (7, 3), (9, 7)}),
"Together": Relation("Together", 2, {(0, 12), (2, 1), (4, 3), (5, 3), (6, 3), (8, 7)}),
    },
"US10_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (7, 4)}),
"Together": Relation("Together", 2, set()),
    },
"US10_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4), (6, 5), (7, 6), (10, 7), (12, 10)}),
"Together": Relation("Together", 2, {(0, 16), (1, 16), (8, 7), (9, 7), (11, 10), (13, 12)}),
    },
"US10_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(0, 2)}),
    },
"US10_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(0, 1)}),
    },
"US10_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2)}),
"Together": Relation("Together", 2, {(0, 7), (5, 4)}),
    },
"US10_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
"Together": Relation("Together", 2, {(2, 1), (0, 9), (4, 3), (6, 5) ,(7, 5), (8, 5)}),
    },
"US10_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4), (7, 5), (8, 7), (10, 8), (11, 10), (12, 11), (13, 12)}),
"Together": Relation("Together", 2, {(0, 14), (6, 5), (9, 8)}),
    },
"US10_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (7, 5), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(0, 11), (2, 3), (6, 5)}),
    },
"US10_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (7, 5), (8, 7)}),
"Together": Relation("Together", 2, {(0, 10), (3, 2), (6, 5), (9, 8)}),
    },
"US10_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(0, 8), (4, 3), (5, 3), (6, 3), (7, 3)}),
    },
}