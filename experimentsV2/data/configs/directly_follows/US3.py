from src.custom_classes.Relation import Relation

config = {
    "US3_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US3_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(4, 3)}),
    },
"US3_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 3), (5, 2), (7, 5), (6, 7), (9, 6)}),
"Together": Relation("Together", 2, {(4, 2), (8, 7)}),
    },
"US3_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(11, 1), (12, 5)}),
    },
"US3_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, set()),
    },
"US3_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US3_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4)}),
    },
"US3_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(6, 5), (8, 7)}),
    },
"US3_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4), (8, 7)}),
    },
"US3_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4), (8, 6), (9, 7)}),
    },
"US3_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6), (9, 7)}),
"Together": Relation("Together", 2, {(5, 4), (8, 7), (10, 9)}),
    },
"US3_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(9, 8)}),
    },
"US3_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (8, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6)}),
    },
"US3_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (9, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (8, 6), (10, 9)}),
    },
"US3_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (7, 5), (9, 7)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (8, 7)}),
    },
"US3_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (8, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (9, 8)}),
    },
"US3_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (8, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6)}),
    },
"US3_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(3, 2), (6, 5), (8, 7), (9, 7)}),
    },
"US3_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4)}),
    },
"US3_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"US3_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4), (8, 7)}),
    },
"US3_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (8, 5)}),
"Together": Relation("Together", 2, {(6, 4), (7, 5)}),
    },
"US3_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6)}),
"Together": Relation("Together", 2, {(5, 4)}),
    },
}