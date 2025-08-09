from src.custom_classes.Relation import Relation

config = {
    "SS7_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 1)}),
    },
"SS7_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (12, 9)}),
"Together": Relation("Together", 2, {(2, 1), (10, 9), (11, 12)}),
    },
"SS7_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(8, 7)}),
    },
"SS7_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, set()),
    },
"SS7_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(8, 7), (9, 8), (11, 9)}),
"Together": Relation("Together", 2, {(10, 9), (2, 14), (4, 12), (3, 18)}),
    },
"SS7_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 2)}),
    },
"SS7_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (7, 6), (8, 6)}),
    },
"SS7_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 7), (2, 1), (8, 2), (3, 8), (4, 3), (9, 4), (5, 9), (6, 5), (11, 6), (12, 11), (13, 12), (14, 13)}),
"Together": Relation("Together", 2, {(10, 6)}),
    },
"SS7_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (12, 10), (11, 12), (14, 11)}),
"Together": Relation("Together", 2, {(13, 11)}),
    },
"SS7_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3), (4, 2), (5, 4)}),
"Together": Relation("Together", 2, {(6, 5), (7, 5), (8, 5)}),
    },
"SS7_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4),  (7, 5), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(2, 1), (6, 5)}),
    },
"SS7_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
"Together": Relation("Together", 2, {(5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15)}),
    },
"SS7_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (10, 9)}),
    },
"SS7_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 3)}),
    },
"SS7_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4), (8, 5), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(3, 2), (6, 5), (7, 8)}),
    },
"SS7_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 3), (4, 2), (5, 4), (6, 5), (7, 6), (9, 7), (10, 9)}),
"Together": Relation("Together", 2, {(1, 3), (8, 7)}),
    },
"SS7_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (6, 5), (7, 6), (10, 7)}),
"Together": Relation("Together", 2, {(3, 2), (8, 7), (9, 7)}),
    },
"SS7_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 20), (2, 18), (3, 16), (4, 14), (5, 12), (6, 26), (7, 26), (8, 24), (9, 24), (10, 22), (11, 22)}),
    },
"SS7_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4)}),
    },
"SS7_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
"Together": Relation("Together", 2, set()),
    },
"SS7_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_28": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3), (10, 9)}),
    },
"SS7_29": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 4)}),
    },
"SS7_30": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"SS7_31": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (10, 4), (11, 7), (4, 10), (5, 10), (6, 9), (7, 11), (8, 11)}),
    },
"SS7_32": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_33": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_34": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_35": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
"Together": Relation("Together", 2, set()),
    },
"SS7_36": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)}),
    },
"SS7_37": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (2, 15), (9, 12)}),
    },
"SS7_38": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 3), (7, 6)}),
"Together": Relation("Together", 2, {(2, 1)}),
    },
"SS7_39": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"SS7_40": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14)}),
"Together": Relation("Together", 2, {(2, 0), (16, 15), (17, 15), (18, 15)}),
    },
"SS7_41": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, {(6, 5)}),
    },
"SS7_42": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
"Together": Relation("Together", 2, {(2, 1), (4, 3)}),
    },
}