from src.custom_classes.Relation import Relation

config = {
    "BS7_2_short_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_short_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_short_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1)}),
    },
"BS7_2_short_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1)}),
    },
"BS7_2_short_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_short_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (4, 3), (6, 4), (7, 6)}),
    },
"BS7_2_short_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (4, 3), (6, 4), (7, 6)}),
    },
"BS7_2_short_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_short_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_short_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS7_2_short_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"BS7_2_short_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4)}),
    },
}