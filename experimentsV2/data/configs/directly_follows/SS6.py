from src.custom_classes.Relation import Relation


config = {
    "SS6_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "SS6_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 1), (2, 5), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(6, 1)}),
    },
    "SS6_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4), (8, 6)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (7, 6)}),
    },
    "SS6_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "SS6_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "SS6_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
    "SS6_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 1), (2, 5), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(6, 2)}),
    },
    "SS6_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
    "SS6_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, set()),
    },
    "SS6_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (8, 18), (9, 18), (10, 18), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 18)}),
    },
    "SS6_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(0, 2), (3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 4)}),
    },
    "SS6_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11)}),
"Together": Relation("Together", 2, {(13, 4), (14, 5), (15, 6)}),
    },
"SS6_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(0, 2), (3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 6)}),
    },
"SS6_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5), (8, 7)}),
"Together": Relation("Together", 2, {(6, 5)}),
    },
"SS6_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14)}),
    },
"SS6_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(0, 2), (3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 7)}),
    },
"SS6_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_28": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_29": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS6_30": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (4, 1), (5, 1)}),
    },
"SS6_31": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, set()),
    },
"SS6_32": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(0, 2), (3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(10, 8)}),
    },
"SS6_33": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(4, 3)}),
    },
"SS6_34": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (8, 6), (9, 8), (10, 9), (11, 10)}),
"Together": Relation("Together", 2, {(7, 8)}),
    },
}