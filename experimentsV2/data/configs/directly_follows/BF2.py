from src.custom_classes.Relation import Relation

config = {
    "BF2_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, set()),
"Together": Relation("Together", 2, set()),
    },
    "BF2_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 0), (12, 1), (12, 2), (12, 3)}),
"Together": Relation("Together", 2, set()),
    },
    "BF2_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 0), (12, 1), (12, 2), (12, 3), (13, 0), (13, 1), (13, 2), (13, 3), (13, 12)}),
"Together": Relation("Together", 2, set()),
    },
"BF2_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(12, 0), (12, 1), (12, 2), (13, 0), (13, 1), (13, 2), (13, 12), (12, 3), (13, 3)}),
"Together": Relation("Together", 2, set()),
    },
"BF2_4": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6)}),
"Together": Relation("Together", 2, set()),
    },
"BF2_5": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6)}),
"Together": Relation("Together", 2, set()),
    },
"BF2_6": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(11, 0), (11, 1), (11, 2), (12, 0), (12, 1), (12, 2), (12, 11)}),
"Together": Relation("Together", 2, set()),
    },
"BF2_7": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(13, 0), (13, 1), (13, 2), (13, 3), (13, 4)}),
"Together": Relation("Together", 2, set()),
    },
}