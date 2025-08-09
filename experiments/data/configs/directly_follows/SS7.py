from src.custom_classes.Relation import Relation

config = {
    "SS7_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (12, 9)})
    },
"SS7_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
"SS7_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
"SS7_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(8, 7), (9, 8), (11, 9)}),
    },
"SS7_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4)}),
    },
"SS7_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 7), (2, 1), (8, 2), (3, 8), (4, 3), (9, 4), (5, 9), (6, 5), (11, 6), (12, 11), (13, 12), (14, 13)}),
    },
"SS7_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (12, 10), (11, 12), (14, 11)}),
    },
"SS7_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3), (4, 2), (5, 4)}),
    },
"SS7_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4),  (7, 5), (8, 7), (9, 8), (10, 9)}),
    },
"SS7_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
    },
"SS7_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8)}),
    },
"SS7_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4), (8, 5), (9, 8), (10, 9)}),
    },
"SS7_17": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 3), (4, 2), (5, 4), (6, 5), (7, 6), (9, 7), (10, 9)}),
    },
"SS7_18": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (6, 5), (7, 6), (10, 7)}),
    },
"SS7_19": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_20": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (4, 2)}),
    },
"SS7_21": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_22": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_23": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_24": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
    },
"SS7_25": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_26": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_27": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_28": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8)}),
    },
"SS7_29": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_30": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_31": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_32": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_33": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_34": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_35": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)}),
    },
"SS7_36": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_37": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_38": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 4), (6, 3), (7, 6)}),
    },
"SS7_39": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"SS7_40": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 0), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14)}),
    },
"SS7_41": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"SS7_42": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
    },
}