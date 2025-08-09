from src.custom_classes.Relation import Relation

config = {
    "US9_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US9_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (7, 6), (8, 6)}),
    },
"US9_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (6, 4), (7, 6), (10, 7), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15), (17, 16)}),
"Together": Relation("Together", 2, {(5, 4), (8, 7), (9, 7), (20, 11)}),
    },
"US9_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US9_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (5, 4), (2, 5), (6, 2), (7, 6), (8, 7), (10, 8), (11, 10), (12, 11), (16, 12), (13, 16), (14, 13), (15, 14)}),
"Together": Relation("Together", 2, {(9, 8)}),
    },
"US9_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 2), (7, 6)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (5, 2), (8, 6), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7)}),
    },
"US9_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (5, 3), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(4, 3)}),
    },
"US9_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (6, 4)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6)}),
    },
"US9_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)}),
    },
"US9_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US9_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2)}),
"Together": Relation("Together", 2, set()),
    },
"US9_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}