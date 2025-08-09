from src.custom_classes.Relation import Relation

config = {
    "BS12_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS12_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
"BS12_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set())
    },
"BS12_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 10), (12, 11), (13, 12)}),
    },
"BS12_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS12_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS12_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2)}),
    },
"BS12_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
"BS12_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5)}),
    },
"BS12_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS12_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (7, 4)}),
    },
"BS12_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (6, 4), (9, 6), (10, 9), (11, 10)}),
    },
"BS12_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (2, 3)}),
    },
"BS12_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 5), (2, 1), (3, 2), (4, 3), (7, 4)}),
    },
"BS12_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}