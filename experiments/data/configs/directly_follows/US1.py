from src.custom_classes.Relation import Relation

config = {
    "US1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
    },
"US1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (10, 6), (8, 10), (9, 8)})
    },
"US1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (11, 8), (9, 11), (10, 9)}),
    },
"US1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US1_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11)}),
    },
"US1_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(17, 15), (19, 17)}),
    },
}