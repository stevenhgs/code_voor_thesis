from src.custom_classes.Relation import Relation


config = {
    "tree_example": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (7, 4)}),
        "Together": Relation("DirectlyFollows", 2, {(9, 1), (10, 4), (3, 4), (11, 7), (6, 7)}),
    },
    "bullet_points": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3)}),
        "Together": Relation("DirectlyFollows", 2, set()),
    }
}