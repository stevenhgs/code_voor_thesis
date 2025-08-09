from src.custom_classes.Relation import Relation

config = {
    "US2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"US2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8), (13, 9), (14, 13), (15, 14)}),
"Together": Relation("Together", 2, {(4, 3), (10, 7), (11, 8), (12, 9)}),
    },
"US2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (9, 4), (5, 9), (11, 5), (12, 11), (13, 12)}),
"Together": Relation("Together", 2, {(6, 2), (7, 3), (8, 4), (10, 5), (14, 13), (15, 13), (16, 13), (17, 13)}),
    },
"US2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (9, 5), (10, 9), (11, 10), (12, 11)}),
"Together": Relation("Together", 2, {(6, 9), (7, 10), (8, 11), (13, 12), (14, 12)}),
    },
"US2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (5, 2), (7, 5), (10, 7)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (6, 5), (8, 7), (9, 7), (11, 10), (12, 10), (13, 10), (14, 10)}),
    },
"US2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 1), (7, 5), (9, 7)}),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (4, 1), (6, 5), (8, 7), (10, 9)}),
    },
"US2_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (6, 4)}),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (5, 4), (7, 6), (8, 6), (9, 6), (14, 8)}),
    },
"US2_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(6, 0), (7, 1), (8, 2)}),
    },
}