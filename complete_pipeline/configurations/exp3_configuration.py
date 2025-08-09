from src.custom_classes.Relation import Relation


config = {
    "exp3_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
    "exp3_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3)}),
    },
    "exp3_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (5, 6)}),
    },
    "exp3_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
    "exp3_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (5, 8)}),
    },
    "exp3_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
    "exp3_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
    "exp3_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 6), (12, 9), (15, 12), (18, 15)}),
    },
    "exp3_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (3, 2), (2, 1)}),
    },
    "exp3_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4), (10, 7)}),
    },
    "exp3_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
    "exp3_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
    },
    "exp3_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
    },
    "exp3_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1)}),
    },
    "exp3_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(8, 1), (5, 8)}),
    },
}
