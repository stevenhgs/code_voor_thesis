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
    },
    "slide_deck_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2)})
    },
    "slide_deck_1": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(9, 6), (12, 9), (15, 12), (18, 15)}),
        # "DirectlyFollows2": Relation("DirectlyFollows", 2, {(2, 1), (4, 2), (5, 4), (3, 5)})
    },
    "slide_deck_2": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (4, 3), (5, 4)})
    },
    "slide_deck_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(10, 7), (13, 10), (18, 15), (21, 18)}),
        # "DirectlyFollows2": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 4), (6, 5)})
    },
    "dummy_0": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)}),
    },
    "dummy_3": {
        "DirectlyFollows": Relation("DirectlyFollows", 2, {(1, 0), (2, 1), (3, 2), (4, 3)}),
        # "DirectlyFollows2": Relation("DirectlyFollows", 2, {(2, 1), (3, 2), (5, 4), (6, 5)})
    }


}
