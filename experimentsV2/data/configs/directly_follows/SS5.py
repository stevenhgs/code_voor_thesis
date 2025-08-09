from src.custom_classes.Relation import Relation

config = {
    "SS5_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (2, 4), (5, 2), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(3, 6)}),
    },
"SS5_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(9, 8)}),
    },
"SS5_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(15, 14), (16, 15), (17, 16)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (9, 7), (10, 9), (11, 10), (13, 11)}),
"Together": Relation("Together", 2, {(2, 1), (8, 7), (12, 11)}),
    },
"SS5_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2)}),
    },
"SS5_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4)}),
    },
"SS5_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2)}),
    },
"SS5_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (10, 8), (11, 10), (12, 11)}),
"Together": Relation("Together", 2, {(9, 8)}),
    },
"SS5_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (7, 6), (8, 6)}),
    },
"SS5_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4)}),
    },
"SS5_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS5_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(6, 5)}),
    },
"SS5_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (6, 5), (7, 5)}),
    },
"SS5_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5)}),
"Together": Relation("Together", 2, {(4, 3), (2, 3), (7, 6), (8, 6)}),
    },
"SS5_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (9, 8)}),
    },
"SS5_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_28": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 3), (4, 2), (5, 4), (8, 5), (6, 8), (9, 6), (10, 9)}),
"Together": Relation("Together", 2, {(1, 3), (7, 9)}),
    },
"SS5_29": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (9, 6), (12, 9)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (7, 6), (8, 6), (10, 9), (11, 9), (13, 12)}),
    },
"SS5_30": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS5_31": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (8, 5), (9, 8)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (7, 8)}),
    },
"SS5_32": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"SS5_33": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
}