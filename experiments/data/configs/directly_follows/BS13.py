from src.custom_classes.Relation import Relation

config = {
    "BS13_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (13, 4), (8, 6), (9, 8)}),
    },
"BS13_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)})
    },
"BS13_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2)}),
    },
"BS13_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"BS13_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}