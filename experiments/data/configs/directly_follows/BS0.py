from src.custom_classes.Relation import Relation


config = {
    "BS0_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
    "BS0_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4)}),
    },
"BS0_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (8, 6)}),
    },
"BS0_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 2)}),
    },
"BS0_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4)}),
    },
"BS0_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (7, 5), (8, 7)}),
    },
"BS0_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (7, 5)}),
    },
"BS0_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)}),
    },
"BS0_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS0_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}