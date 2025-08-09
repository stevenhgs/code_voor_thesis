from collections import defaultdict
from math import sqrt, inf
from src.arrow_recognition.arrow_recognition import find_arrow_from_list_of_points
from src.custom_classes.Relation import Relation
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from keyword import iskeyword


def get_objects_id_to_objects_and_all_objects(input_file_name, xml_directory_path):
    xml_input_path = f"{xml_directory_path}{input_file_name}.xml"
    object_id_to_object = get_objects_from_xml_file_path(xml_input_path)

    # get object ids to object
    # double shape problem
    new_object_id_to_object = dict()
    seen = set()
    for object_id, object in object_id_to_object.items():
        if object["type"] == "curve":
            if tuple(object["pts"]) not in seen:
                new_object_id_to_object[object_id] = object
                seen.add(tuple(object["pts"]))
        else:
            new_object_id_to_object[object_id] = object

    object_id_to_object = new_object_id_to_object
    all_objects = set(object_id_to_object.keys())
    return object_id_to_object, all_objects


def get_spatial_relation(bbox1, bbox2, in_y_direction):
    direction_indicators = ["XDim", "YDim"]
    lower1, upper1 = bbox1[0][in_y_direction], bbox1[1][in_y_direction]
    lower2, upper2 = bbox2[0][in_y_direction], bbox2[1][in_y_direction]
    if lower1 == lower2 and upper1 == upper2:
        return direction_indicators[in_y_direction] + "Equals"
    if upper1 <= lower2:
        return direction_indicators[in_y_direction] + "Before"
    if lower1 <= lower2 and upper1 <= upper2:
        return direction_indicators[in_y_direction] + "OverlapsStart"
    if lower1 <= lower2 and upper2 <= upper1:
        return direction_indicators[in_y_direction] + "Covers"
    return None


def get_distance_between_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def get_closest_bbox_to_point(object_id_to_object, point, point_from_id):
    x, y = point
    closest_id, closest_point, closest_distance = None, None, inf
    for object_id, val in object_id_to_object.items():
        if object_id == point_from_id:
            continue
        (bottom_left_x, bottom_left_y), (top_right_x, top_right_y) = val['bbox']
        if bottom_left_x <= x <= top_right_x and bottom_left_y <= y <= top_right_y:
            continue
        if x <= bottom_left_x:
            anchor_x = bottom_left_x
        elif x >= top_right_x:
            anchor_x = top_right_x
        else:
            anchor_x = x
        if y <= bottom_left_y:
            anchor_y = bottom_left_y
        elif y >= top_right_y:
            anchor_y = top_right_y
        else:
            anchor_y = y

        dist = sqrt((anchor_x - x)**2 + (anchor_y - y)**2)
        if dist < closest_distance:
            closest_id = object_id
            closest_point = (anchor_x, anchor_y)
            closest_distance = dist

    return closest_id, closest_point


def get_closest_bbox_to_point_with_in(object_id_to_object, point, point_from_id):
    x, y = point
    closest_id, closest_point, closest_distance = None, None, inf
    for object_id, val in object_id_to_object.items():
        if object_id == point_from_id:
            continue
        (bottom_left_x, bottom_left_y), (top_right_x, top_right_y) = val['bbox']
        if bottom_left_x <= x <= top_right_x and bottom_left_y <= y <= top_right_y:
            if abs(x - bottom_left_x) < abs(x - top_right_x):
                anchor_x = bottom_left_x
            else:
                anchor_x = top_right_x
            if abs(y - bottom_left_y) < abs(y - top_right_y):
                anchor_y = bottom_left_y
            else:
                anchor_y = top_right_y

            dist_x = min(abs(x - bottom_left_x), abs(x - top_right_x))
            dist_y = min(abs(y - bottom_left_y), abs(y - top_right_y))
            if dist_x < dist_y:
                anchor_y = y
            else:
                anchor_x = x
            dist = min(dist_x, dist_y)
        else:
            if x <= bottom_left_x:
                anchor_x = bottom_left_x
            elif x >= top_right_x:
                anchor_x = top_right_x
            else:
                anchor_x = x
            if y <= bottom_left_y:
                anchor_y = bottom_left_y
            elif y >= top_right_y:
                anchor_y = top_right_y
            else:
                anchor_y = y

            dist = sqrt((anchor_x - x)**2 + (anchor_y - y)**2)

        if dist < closest_distance:
            closest_id = object_id
            closest_point = (anchor_x, anchor_y)
            closest_distance = dist

    return closest_id, closest_point


def get_distance_between_two_bbox(bbox1, bbox2):
    """
    Precondition: assumes bbox1 and bbox2 do not overlap.
    """
    (bottom_left_x1, bottom_left_y1), (top_right_x1, top_right_y1) = bbox1
    (bottom_left_x2, bottom_left_y2), (top_right_x2, top_right_y2) = bbox2
    closest_x1, closest_y1 = None, None
    closest_x2, closest_y2 = None, None

    # Handle XDim
    # covers: XDimBefore(x2, x1)
    if top_right_x2 <= bottom_left_x1:
        closest_x1 = bottom_left_x1
        closest_x2 = top_right_x2
    # covers: OverlapsStart(x2, x1)
    elif bottom_left_x1 <= top_right_x2 <= top_right_x1:
        closest_x1 = top_right_x2
        closest_x2 = top_right_x2
    # covers: Covers(x2, x1)
    elif bottom_left_x2 <= bottom_left_x1 and  top_right_x1 <= top_right_x2:
        closest_x1 = bottom_left_x1
        closest_x2 = bottom_left_x1
    # covers: XDimBefore(x1, x2)
    elif top_right_x1 <= bottom_left_x2:
        closest_x1 = top_right_x1
        closest_x2 = bottom_left_x2
    # covers: OverlapsStart(x1, x2)
    elif bottom_left_x2 <= top_right_x1 <= top_right_x2:
        closest_x1 = top_right_x1
        closest_x2 = top_right_x1
    # covers: Covers(x1, x2)
    elif bottom_left_x1 <= bottom_left_x2 and top_right_x2 <= top_right_x1:
        closest_x1 = bottom_left_x2
        closest_x2 = bottom_left_x2

    # Handle YDim
    # covers: YDimBefore(x2, x1)
    if top_right_y2 <= bottom_left_y1:
        closest_y1 = bottom_left_y1
        closest_y2 = top_right_y2
    # covers: OverlapsStart(x2, x1)
    elif bottom_left_y1 <= top_right_y2 <= top_right_y1:
        closest_y1 = top_right_y2
        closest_y2 = top_right_y2
    # covers: Covers(x2, x1)
    elif bottom_left_y2 <= bottom_left_y1 and top_right_y1 <= top_right_y2:
        closest_y1 = bottom_left_y1
        closest_y2 = bottom_left_y1
    # covers: YDimBefore(x1, x2)
    elif top_right_y1 <= bottom_left_y2:
        closest_y1 = top_right_y1
        closest_y2 = bottom_left_y2
    # covers: OverlapsStart(x1, x2)
    elif bottom_left_y2 <= top_right_y1 <= top_right_y2:
        closest_y1 = top_right_y1
        closest_y2 = top_right_y1
    # covers: Covers(x1, x2)
    elif bottom_left_y1 <= bottom_left_y2 and top_right_y2 <= top_right_y1:
        closest_y1 = bottom_left_y2
        closest_y2 = bottom_left_y2

    return get_distance_between_two_points((closest_x1, closest_y1), (closest_x2, closest_y2))

def get_closest_candidate_bbox(object_id_to_object, reference_object_id, candidate_object_ids):
    ref_bbox = object_id_to_object[reference_object_id]["bbox"]
    closest_distance = inf
    closest_candidate_id = None
    for candidate_object_id in candidate_object_ids:
        candidate_bbox = object_id_to_object[candidate_object_id]["bbox"]
        candidate_distance = get_distance_between_two_bbox(ref_bbox, candidate_bbox)
        if candidate_distance < closest_distance:
            closest_distance = candidate_distance
            closest_candidate_id = candidate_object_id
    return closest_candidate_id


def does_overlap(bbox1, bbox2):
    (start_x1, start_y1), (end_x1, end_y1) = bbox1
    (start_x2, start_y2), (end_x2, end_y2) = bbox2
    x_dim_overlap = start_x1 <= start_x2 <= end_x1 or start_x1 <= end_x2 <= end_x1
    y_dim_overlap = start_y1 <= start_y2 <= end_y1 or start_y1 <= end_y2 <= end_y1
    return x_dim_overlap and y_dim_overlap


def get_closest_under(reference_object_id, candidate_object_ids):
    """
    Depth is based on object_id.
    Smaller object ids are behind larger object ids.
    """
    closest_under = None
    for candidate_object_id in candidate_object_ids:
        if candidate_object_id < reference_object_id and (closest_under is None or closest_under < candidate_object_id):
            closest_under = candidate_object_id
    return closest_under


def get_base_predicates_from_objects(object_id_to_object):
    """
    base_predicates:
    * ALlen's interval algebra in XDim and YDim:
    1) Before(x, y)
    2) OverlapsStart(x, y)
    3) Covers(x, y)
    4) Equals(x, y)
    Extra:
    6) 2DimCovers(x, y)
    * 3D:
    7) OnTop(x, y)
    * Content:
    8) InBulletPoint(x)
    9) InEnumeration(x)
    * Arrow related:
    10) IsArrow(x)
    11) AtBaseOfArrow(x,a)
    12) AtTipOfArrow(x,a)
    """
    # print(f'from get_base_predicates_from_objects: {object_id_to_object}')
    object_ids = list(object_id_to_object)
    object_ids_size = len(object_ids)
    relations = defaultdict(set)

    for i in range(object_ids_size):
        object1 = object_id_to_object[object_ids[i]]
        # bullet point relation
        if object1["type"] == "Text" and len(object1["text"]) > 0:
            first_word = object1["text"].split(' ')[0]
            if len(first_word) > 1 and first_word[:-1].isdigit() and not first_word[-1].isdigit() and ord(first_word[-1]) > 31 and first_word[-1] not in [':', ',', '%']:
                # print('InEnumeration', object1["text"], ord(first_word[-1]))
                relations['InEnumeration'].add((object_ids[i],))
            if len(object1["text"]) > 1 and object1["text"][0] in ['•', '›', '–', '◼', '▪', '❑']:
                relations['InBulletPoint'].add((object_ids[i], ))

            relations['Text'].add((object_ids[i], ))
            if object1["Bold"]:
                relations['Bold'].add((object_ids[i], ))
        elif object1["type"] == "curve":
            tip_of_arrow, base_of_arrow = find_arrow_from_list_of_points(object1["pts"])
            if tip_of_arrow is not None:
                relations["Arrow"].add((object_ids[i], ))
                relations["TipOfArrow"].add((object_ids[i], tip_of_arrow))
                at_tip_of_arrow_id, at_tip_of_arrow_closest_point = get_closest_bbox_to_point(object_id_to_object, tip_of_arrow, object_ids[i])
                relations["AtTipOfArrow"].add(((at_tip_of_arrow_id, object_ids[i]), (at_tip_of_arrow_closest_point, tip_of_arrow)))
                relations["BaseOfArrow"].add((object_ids[i], base_of_arrow))
                at_base_of_arrow_id, at_base_of_arrow_closest_point = get_closest_bbox_to_point_with_in(object_id_to_object, base_of_arrow, object_ids[i])
                relations["AtBaseOfArrow"].add(((at_base_of_arrow_id, object_ids[i]), (at_base_of_arrow_closest_point, base_of_arrow)))
            else:
                relations["Curve"].add((object_ids[i], ))
        elif object1["type"] == "image":
            relations["Image"].add((object_ids[i],))

        for j in range(object_ids_size):
            if i == j:
                continue
            object2 = object_id_to_object[object_ids[j]]

            # spatial relations
            x_dim_spatial_relation = get_spatial_relation(object1["bbox"], object2["bbox"], in_y_direction=False)
            if x_dim_spatial_relation is not None:
                relations[x_dim_spatial_relation].add((object_ids[i], object_ids[j]))
            y_dim_spatial_relation = get_spatial_relation(object1["bbox"], object2["bbox"], in_y_direction=True)
            if y_dim_spatial_relation is not None:
                relations[y_dim_spatial_relation].add((object_ids[i], object_ids[j]))

            # overlap relation
            if does_overlap(object1["bbox"], object2["bbox"]):
                relations["Overlap"].add((object_ids[i], object_ids[j]))
                relations["Overlap"].add((object_ids[j], object_ids[i]))

            # 3D relations
            if object1["obj_counter"] > object2["obj_counter"]:
                relations["OnTop"].add((object_ids[i], object_ids[j]))

        for pair in relations["XDimCovers"]:
            if pair in relations["YDimCovers"]:
                relations["2DimCovers"].add(pair)

        # remove relations if empty after touching them in previous loops
        if len(relations["XDimCovers"]) == 0:
            del relations["XDimCovers"]
        if len(relations["YDimCovers"]) == 0:
            del relations["YDimCovers"]

    if len(relations["YDimBefore"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        for id1, id2 in relations["YDimBefore"]:
            ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_candidate_bbox(object_id_to_object, ref_object_id, candidate_ids)
            relations["YDimBeforeClosest"].add((ref_object_id, closest_candidate_id))
    else:
        del relations["YDimBefore"]

    if len(relations["XDimBefore"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        for id1, id2 in relations["XDimBefore"]:
            ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_candidate_bbox(object_id_to_object, ref_object_id, candidate_ids)
            relations["XDimBeforeClosest"].add((ref_object_id, closest_candidate_id))
    else:
        del relations["XDimBefore"]

    if len(relations["Overlap"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        for id1, id2 in relations["Overlap"]:
            ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_under(ref_object_id, candidate_ids)
            if closest_candidate_id is None:
                continue
            relations["ClosestUnderAndOverlap"].add((closest_candidate_id, ref_object_id))
    else:
        del relations["Overlap"]

    if len(relations["2DimCovers"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        for id1, id2 in relations["2DimCovers"]:
            ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_under(ref_object_id, candidate_ids)
            if closest_candidate_id is None:
                continue
            relations["ClosestUnderAnd2DimCovered"].add((closest_candidate_id, ref_object_id))
    else:
        del relations["2DimCovers"]

    if len(relations["Bold"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        for id1, id2 in relations["YDimBefore"]:
            if (id2,) in relations["Bold"]:
                ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_candidate_bbox(object_id_to_object, ref_object_id, candidate_ids)
            relations["ClosestYDimAfterAndBold"].add((closest_candidate_id, ref_object_id))
    else:
        del relations["Bold"]

    if len(relations["InBulletPoint"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        if relations.get("YDimBefore") is not None:
            for id1, id2 in relations["YDimBefore"]:
                if (id2,) in relations["InBulletPoint"]:
                    ref_object_id_to_candidate_ids[id1].append(id2)
        if relations.get("YDimOverlapsStart") is not None:
            for id1, id2 in relations["YDimOverlapsStart"]:
                if (id2,) in relations["InBulletPoint"]:
                    ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_candidate_bbox(object_id_to_object, ref_object_id, candidate_ids)
            relations["ClosestYDimAfterAndInBulletPoint"].add((closest_candidate_id, ref_object_id))
    else:
        del relations["InBulletPoint"]

    if len(relations["InEnumeration"]) != 0:
        ref_object_id_to_candidate_ids = defaultdict(list)
        if relations.get("YDimBefore") is not None:
            for id1, id2 in relations["YDimBefore"]:
                if (id2,) in relations["InEnumeration"]:
                    ref_object_id_to_candidate_ids[id1].append(id2)
        if relations.get("YDimOverlapsStart") is not None:
            for id1, id2 in relations["YDimOverlapsStart"]:
                if (id2,) in relations["InEnumeration"]:
                    ref_object_id_to_candidate_ids[id1].append(id2)
        for ref_object_id, candidate_ids in ref_object_id_to_candidate_ids.items():
            closest_candidate_id = get_closest_candidate_bbox(object_id_to_object, ref_object_id, candidate_ids)
            relations["ClosestYDimAfterAndInEnumeration"].add((closest_candidate_id, ref_object_id))
    else:
        del relations["InEnumeration"]

    """
    allowed_base_predicates = {
        "XDimEquals",
        "XDimBefore",
        "XDimOverlapsStart",
        "XDimCovers",
        "YDimEquals",
        "YDimBefore",
        "YDimOverlapsStart",
        "YDimCovers",
        "OnTop",
        "Overlap",
        "Image",
        "Text",
        "Curve",
        "Arrow",
        "InBulletPoint",
        "InEnumeration",
        "Bold",
    } 
    
    filtered_relations = defaultdict(set)
    for key, val in relations.items():
        if key in allowed_base_predicates:
            filtered_relations[key] = val
    
    relations = filtered_relations
    """

    """
    if relations.get("Bold") is not None:
        del relations["Bold"]
    if relations.get("Arrow") is not None:
        del relations["Arrow"]
    if relations.get("AtTipOfArrow") is not None:
        del relations["AtTipOfArrow"]
    if relations.get("AtBaseOfArrow") is not None:
        del relations["AtBaseOfArrow"]
    if relations.get("OnTop") is not None:
        del relations["OnTop"]
    """
    return relations


def get_base_relation_name_to_relation_dict(object_id_to_object):
    relations = get_base_predicates_from_objects(object_id_to_object)
    base_relation_name_to_relation_dict = dict()

    for relation_name, examples in relations.items():
        if relation_name == "TipOfArrow" or relation_name == "BaseOfArrow":
            continue
        elif relation_name == "AtTipOfArrow" or relation_name == "AtBaseOfArrow":
            base_relation_name_to_relation_dict[relation_name] = Relation(relation_name, 2, {e[0] for e in examples})
        else:
            base_relation_name_to_relation_dict[relation_name] = Relation(relation_name, len(list(examples)[0]), set(examples))

    return base_relation_name_to_relation_dict
