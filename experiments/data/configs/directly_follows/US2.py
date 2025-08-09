from src.custom_classes.Relation import Relation

config = {
    "US2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
    },
"US2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8), (13, 9), (14, 13), (15, 14)})
    },
"US2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (9, 4), (5, 9), (11, 5), (12, 11), (13, 12)}),
    },
"US2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (9, 5), (10, 9), (11, 10), (12, 11)}),
    },
"US2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (5, 2), (7, 5), (10, 7)}),
    },
"US2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
"US2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 1), (7, 5), (9, 7)}),
    },
"US2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (6, 4)}),
    },
"US2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
    },
}