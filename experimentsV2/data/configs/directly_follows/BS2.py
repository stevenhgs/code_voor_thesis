from src.custom_classes.Relation import Relation

config = {
    "BS2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "BS2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, set()),
    },
    "BS2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 4), (2, 5), (3, 5)}),
    },
"BS2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(1, 9), (2, 10), (3, 10)}),
    },
"BS2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (12, 10), (13, 12)}),
"Together": Relation("Together", 2, {(1, 15), (2, 16), (3, 16), (11, 10), (14, 13)}),
    },
"BS2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"BS2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"BS2_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(5, 4)}),
    },
"BS2_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS2_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (6, 5)}),
"Together": Relation("Together", 2, {(7, 6), (8, 7)}),
    },
"BS2_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS2_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(4, 3), (8, 6), (9, 7)}),
    },
"BS2_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (7, 3), (8, 7)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (5, 3), (6, 4), (9, 7), (10, 8)}),
    },
"BS2_28": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
"Together": Relation("Together", 2, {(3, 1), (4, 2)}),
    },
"BS2_29": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, set()),

    },
"BS2_30": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 3), (2, 4)}),
    },
"BS2_31": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (6, 4), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(1, 11), (2, 12), (5, 4)}),
    },
"BS2_32": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_33": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (8, 7)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5)}),
    },
"BS2_34": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (8, 7), (9, 8), (11, 9), (13, 11)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (10, 9), (12, 11)}),
    },
"BS2_35": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_36": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_37": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(4, 3), (11, 8), (12, 10)}),
    },
"BS2_38": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_39": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS2_40": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(2, 1), (6, 3), (7, 4), (8, 5)}),
    },
"BS2_41": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BS2_42": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3)}),
"Together": Relation("Together", 2, {(2, 1), (5, 3), (6, 4)}),
    },
}