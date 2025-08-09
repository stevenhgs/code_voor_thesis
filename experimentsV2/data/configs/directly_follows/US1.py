from src.custom_classes.Relation import Relation

config = {
    "US1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)}),
"Together": Relation("Together", 2, {(4, 3), (5, 3), (6, 3)}),
    },
"US1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (10, 6), (8, 10), (9, 8)}),
"Together": Relation("Together", 2, {(7, 10), (11, 9), (12, 9), (12, 10), (13, 10)}),
    },
"US1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (11, 8), (9, 11), (10, 9)}),
"Together": Relation("Together", 2, set()),
    },
"US1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US1_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11)}),
"Together": Relation("Together", 2, {(13, 12), (14, 12)}),
    },
"US1_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(17, 15), (19, 17)}),
"Together": Relation("Together", 2, set()),
    },
}