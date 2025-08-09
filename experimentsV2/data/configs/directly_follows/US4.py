from src.custom_classes.Relation import Relation

config = {
    "US4_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US4_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (7, 4), (8, 7)}),
"Together": Relation("Together", 2, {(3, 2), (5, 4), (6, 4), (9, 8), (11, 12)}),
    },
"US4_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (6, 4)}),
"Together": Relation("Together", 2, {(2, 1), (3, 1), (5, 4), (7, 6), (8, 6), (10, 11)}),
    },
"US4_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 17), (4, 19), (5, 19), (6, 19), (7, 21), (8, 21), (9, 21), (10, 20), (11, 20), (12, 22), (13, 22), (15, 16), (3, 18), (2, 23), (3, 23), (4, 23), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), (13, 23), (17, 23), (18, 23), (19, 23), (20, 23), (21, 23), (22, 23)}),
    },
"US4_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (8, 7)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (9, 8), (11, 12)}),
    },
"US4_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US4_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5), (9, 7)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (8, 7), (10, 9), (12, 13)}),
    },
"US4_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US4_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (7, 5)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (9, 10)}),
    },
"US4_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(2, 18), (4, 19), (6, 20), (7, 21), (16, 17)}),
    },
"US4_10": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 2), (8, 5)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (6, 5), (7, 5), (9, 8), (11, 12)}),
    },
"US4_11": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"US4_12": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 3), (8, 5)}),
"Together": Relation("Together", 2, {(4, 3), (6, 5), (7, 5), (9, 8), (11, 12)}),
    },
"US4_13": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (9, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (8, 6), (10, 9), (12, 13)}),
    },
"US4_14": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)}),
"Together": Relation("Together", 2, {(5, 4), (6, 4), (8, 7), (10, 11)}),
    },
"US4_15": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(5, 6)}),
    },
}