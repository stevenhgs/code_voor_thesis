from src.custom_classes.Relation import Relation


config = {
    "exp_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
    "exp_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3)}),
    },
    "exp_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (5, 6)}),
    },
    "exp_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
    "exp_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (5, 8)}),
    },
    "exp_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1)}),
    },
    "exp_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3)}),
    },
    "exp_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
    "exp_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
    "exp_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 6), (12, 9), (15, 12), (18, 15)}),
    },
    "exp_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4), (10, 7)}),
    },
    "exp_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    }
}