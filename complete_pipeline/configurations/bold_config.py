from src.custom_classes.Relation import Relation


config = {
    "exp3_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1)}),
    },
    "exp3_16": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(8, 1), (5, 8)}),
    },
}