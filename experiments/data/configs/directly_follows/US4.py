from src.custom_classes.Relation import Relation

config = {
    "US4_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (8, 7)}),
    },
"US4_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (6, 4)})
    },
"US4_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (8, 7)}),
    },
"US4_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (9, 7)}),
    },
"US4_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5)}),
    },
"US4_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (8, 5)}),
    },
"US4_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US4_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (8, 5)}),
    },
"US4_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (9, 6)}),
    },
"US4_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)}),
    },
"US4_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}