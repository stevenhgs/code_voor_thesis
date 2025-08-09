from src.custom_classes.Relation import Relation

config = {
    "US8_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(7, 0), (9, 1)}),
    },
"US8_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (4, 3), (6, 4), (8, 6), (9, 8), (10, 9)}),
"Together": Relation("Together", 2, {(2, 1), (5, 4), (7, 6), (11, 10), (12, 0)}),
    },
"US8_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (13, 11)}),
"Together": Relation("Together", 2, {(15, 0), (12, 11), (14, 13)}),
    },
"US8_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 0)}),
    },
"US8_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (9, 7)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (6, 4), (8, 7), (10, 9), (11, 9), (12, 9), (14, 9), (13, 7), (15, 10), (16, 11)}),
    },
"US8_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (6, 5), (8, 7), (9, 7), (10, 7), (11, 7), (12, 1), (13, 2), (14, 9), (15, 10)}),
    },
"US8_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(17, 0), (2, 1), (3, 1), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 2), (15, 3), (16, 10)}),
    },
"US8_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 2), (4, 3), (5, 4), (6, 5), (7, 6)}),
"Together": Relation("Together", 2, {(8, 7), (9, 7), (10, 7), (15, 7)}),
    },
"US8_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(9, 2)}),
    },
"US8_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US8_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US8_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US8_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(12, 2)}),
    },
"US8_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US8_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(3, 1), (5, 3), (8, 5), (10, 8)}),
"Together": Relation("Together", 2, {(16, 0), (18, 3), (19, 11), (20, 11), (2, 1), (4, 3), (6, 5), (7, 5), (9, 8), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)}),
    },
}