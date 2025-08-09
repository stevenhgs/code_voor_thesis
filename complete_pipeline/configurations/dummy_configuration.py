from src.custom_classes.Relation import Relation


config = {
    "dummy_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)}),
    },
    "dummy_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)}),
    },
    "dummy_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)}),
    },
    "dummy_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3)}),
    },
    "dummy_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1)}),
    },
    "dummy_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1)}),
    }


}