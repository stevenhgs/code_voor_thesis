from src.custom_classes.Relation import Relation


config = {
    "exp3_0": {
        "Together": Relation("DirectlyFollows", 2, {(1, 0)}),
    },
    "exp3_1": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_2": {
        "Together": Relation("DirectlyFollows", 2,  {(1, 2)}),
    },
    "exp3_3": {
        "Together": Relation("DirectlyFollows", 2, {(1, 3), (2, 4), (5, 4)}),
    },
    "exp3_4": {
        "Together": Relation("DirectlyFollows", 2, {(1, 4), (2, 6), (3, 5), (7, 6), (8, 5)}),
    },
    "exp3_5": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_6": {
        "Together": Relation("DirectlyFollows", 2, {(1, 4), (3, 5), (2, 8), (6, 5), (7, 5)}),
    },
    "exp3_7": {
        "Together": Relation("DirectlyFollows", 2, {(4, 3), (5, 2)}),
    },
    "exp3_8": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_9": {
        "Together": Relation("DirectlyFollows", 2, {(1, 6), (2, 9), (8, 9), (3, 12), (11, 12), (4, 15), (14, 15), (5, 18), (17, 18)}),
    },
    "exp3_10": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_11": {
        "Together": Relation("DirectlyFollows", 2, {(1, 4), (3, 7), (6, 7), (9, 10), (2, 10)}),
    },
    "exp3_12": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_13": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_14": {
        "Together": Relation("DirectlyFollows", 2, set()),
    },
    "exp3_15": {
        "Together": Relation("DirectlyFollows", 2, {(2, 1), (4, 3), (5, 3)}),
    },
    "exp3_16": {
        "Together": Relation("DirectlyFollows", 2, {(2, 1), (3, 1), (4, 1), (9, 8), (6, 5), (7, 5)}),
    },
}
