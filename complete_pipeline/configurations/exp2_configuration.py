from src.custom_classes.Relation import Relation


config = {
    "exp2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
    },
    "exp2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "exp2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3)}),
    },
    "exp2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (5, 6)}),
    },
    "exp2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1)}),
    },
    "exp2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (5, 8)}),
    },
    "exp2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
    "exp2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
    "exp2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 6), (12, 9), (15, 12), (18, 15)}),
    },
    "exp2_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (3, 2), (2, 1)}),
    },
    "exp2_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4), (10, 7)}),
    },
    "exp2_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
    "exp2_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)}),
    },
    "exp2_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
    }
}
