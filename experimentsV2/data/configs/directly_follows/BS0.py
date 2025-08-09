from src.custom_classes.Relation import Relation


config = {
    "BS0_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
        "Together": Relation("Together", 2, set()),
    },
    "BS0_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 3), (5, 4)}),
"Together": Relation("Together", 2, set()),
    },
"BS0_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(6, 4), (8, 6)}),
"Together": Relation("Together", 2, {(5, 4), (7, 6), (9, 8), (10, 8), (1, 11), (2, 12), (3, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12)}),
    },
"BS0_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 2)}),
"Together": Relation("Together", 2, {(3, 2), (4, 2), (5, 2), (6, 2), (5, 10), (8, 7), (9, 7)}),
    },
"BS0_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 2), (5, 4)}),
"Together": Relation("Together", 2, {(3, 2), (6, 5), (7, 10), (12, 11), (9, 11), (8, 11), (7, 5), (8, 5), (9, 5)}),
    },
"BS0_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (7, 5), (8, 7)}),
"Together": Relation("Together", 2, {(6, 5), (9, 11), (13, 12), (10, 12), (9, 8), (10, 8)}),
    },
"BS0_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(5, 4), (7, 5)}),
"Together": Relation("Together", 2, {(6, 5), (8, 10), (12, 11), (9, 11), (8, 11), (8, 7), (9, 7)}),
    },
"BS0_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(7, 4)}),
"Together": Relation("Together", 2, {(5, 4), (6, 4), (8, 7), (9, 7), (10, 7), (10, 18), (1, 11), (2, 12), (3, 12), (14, 12), (15, 12), (16, 12), (17, 12), (13, 12)}),
    },
"BS0_8": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
"BS0_9": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
}