from src.custom_classes.Relation import Relation

config = {
    "BF1_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 0), (11, 1), (11, 2), (11, 3), (11, 4), }),
"Together": Relation("Together", 2, {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
                                     (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
                                     (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)}),
    },
"BF1_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (12, 11), (13, 11), (13, 12)}),
"Together": Relation("Together", 2, {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
                                     (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
                                     (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)}),
    },
"BF1_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
                                     (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
                                     (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)}),
    },
"BF1_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 0), (10, 1), (10, 2), (10, 3), (11, 0), (11, 1), (11, 2), (11, 3), (11, 10)}),
"Together": Relation("Together", 2, {(5, 0), (5, 1), (5, 2), (5, 3),
                                     (6, 0), (6, 1), (6, 2), (6, 3),
                                     (7, 0), (7, 1), (7, 2), (7, 3)}),
    },
"BF1_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 0), (10, 1), (10, 2), (10, 3)}),
"Together": Relation("Together", 2, {(5, 0), (5, 1), (5, 2), (5, 3),
                                     (6, 0), (6, 1), (6, 2), (6, 3),
                                     (7, 0), (7, 1), (7, 2), (7, 3)}),
    },
}