from src.custom_classes.Relation import Relation


config = {
    "tree_example": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(4, 1), (7, 4)}),
        "Together": Relation("Together", 2, {(9, 1), (10, 4), (11, 7), (4, 3), (7, 6)})
    },
    "bullet_point_example": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)})
    },
    "bullet_point_example2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)})
    },
    "bullet_point_example3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)})
    }
}
