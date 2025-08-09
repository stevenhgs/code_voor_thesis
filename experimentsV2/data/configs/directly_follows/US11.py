from src.custom_classes.Relation import Relation

config = {
    "US11_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 9), (16, 12)}),
"Together": Relation("Together", 2, set()),
    },
"US11_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (8, 5), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (7, 5), (11, 10), (13, 15), (1, 12), (0, 12)}),
    },
"US11_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US11_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(8, 10), (11, 3), (0, 7), (1, 7)}),
    },
"US11_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (7, 5), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(6, 5), (13, 15), (0, 12)}),
    },
"US11_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US11_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 1), (9, 6), (13, 9)}),
"Together": Relation("Together", 2, {(0, 16), (17, 19), (20, 15), (2, 1), (3, 1), (4, 1), (5, 1), (7, 6), (8, 6), (10, 9), (11, 9), (12, 9), (14, 13), (15, 13)}),
    },
"US11_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US11_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US11_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (8, 3), (12, 8)}),
"Together": Relation("Together", 2, {(19, 14), (17, 14), (2, 1), (4, 3), (5, 3), (6, 3), (7, 3), (9, 8), (10, 8), (11, 8), (13, 12)}),
    },
"US11_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 6), (8, 7), (9, 8)}),
"Together": Relation("Together", 2, {(0, 12), (13, 15), (10, 9), (11, 9)}),
    },
"US11_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (7, 5), (9, 7), (10, 9), (11, 10), (14, 11), (15, 14)}),
"Together": Relation("Together", 2, {(17, 19), (21, 8), (20, 1), (0, 16), (4, 3), (6, 5), (12, 11), (13, 11)}),
    },
"US11_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (9, 4), (12, 9), (15, 12)}),
"Together": Relation("Together", 2, {(0, 16), (2, 1), (3, 1), (5, 4), (6, 4), (7, 4), (8, 4), (10, 9), (11, 9), (13, 12), (14, 12)}),
    },
}