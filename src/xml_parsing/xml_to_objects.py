import xml.etree.ElementTree as ElementTree


def str_coords_to_tuple_coords(coords_str):
    split_coords_str = coords_str.split(',')
    seen = set()
    arr = []
    for i in range(0, len(split_coords_str), 2):
        point = (float(split_coords_str[i]), float(split_coords_str[i+1]))
        if point in seen:
            continue
        seen.add(point)
        arr.append(point)
    return arr


def is_large_bbox(bbox, bbox_ref):
    """
    Returns True if the ratio of area of bbox1 and area of bbox_ref is greater than threshold.
    """
    threshold = 0.4
    height = abs(bbox[0][1] - bbox[1][1])
    width = abs(bbox[0][1] - bbox[1][1])
    area = height * width
    height_ref = abs(bbox_ref[0][1] - bbox_ref[1][1])
    width_ref = abs(bbox_ref[0][1] - bbox_ref[1][1])
    area_ref = height_ref * width_ref

    return area / area_ref > threshold


def is_page_number(text):
    split_text = text.split(' / ')
    # print('split', split_text)
    if len(split_text) == 2 and split_text[0].isdigit() and split_text[1][:-1].isdigit():
        # print("is page number", text)
        return True
    if text[:-1].isdigit() and int(text[:-1]) <= 150:
        return True
    return False


def get_objects_from_element_tree(node, obj_counter, full_slide_bbox):
    if node.tag == "page":
        full_slide_bbox = str_coords_to_tuple_coords(node.attrib['bbox'])
        output = []
        for child in node:
            output += get_objects_from_element_tree(child, obj_counter + len(output), full_slide_bbox)
        return output
    if node.tag == "textline":
        object = dict()
        object["type"] = "Text"
        object["obj_counter"] = obj_counter
        object["bbox"] = str_coords_to_tuple_coords(node.attrib['bbox'])
        text = ""
        object["first_char_bbox"] = None
        is_bold = False
        for child in node:
            if object["first_char_bbox"] is None:
                object["first_char_bbox"] = str_coords_to_tuple_coords(child.attrib['bbox'])
            if child.attrib.get("font") is not None and "Bold" in child.attrib["font"]:
                is_bold = True
            text += child.text
        object["text"] = text
        object["Bold"] = is_bold
        # print(f'text: {text}')
        # print(object["text"], object["bbox"], full_slide_bbox)
        if is_page_number(text):
            return []
        return [object] if object["bbox"][0][0] <= full_slide_bbox[1][0] and object["bbox"][0][1] <= full_slide_bbox[1][1] else []
    if node.tag == "curve":
        object = dict()
        object["type"] = "curve"
        object["obj_counter"] = obj_counter
        object["bbox"] = str_coords_to_tuple_coords(node.attrib['bbox'])
        object["pts"] = str_coords_to_tuple_coords(node.attrib["pts"])
        return [object] if object["bbox"][0][0] <= full_slide_bbox[1][0] and object["bbox"][0][1] <= full_slide_bbox[1][1] else []
    if node.tag == "rect":
        rect_bbox = str_coords_to_tuple_coords(node.attrib['bbox'])
        if is_large_bbox(rect_bbox, full_slide_bbox):
            return []
        object = dict()
        object["type"] = "curve"
        object["obj_counter"] = obj_counter
        object["bbox"] = str_coords_to_tuple_coords(node.attrib['bbox'])
        object["pts"] = str_coords_to_tuple_coords(node.attrib["bbox"])
        return [object] if object["bbox"][0][0] <= full_slide_bbox[1][0] and object["bbox"][0][1] <= full_slide_bbox[1][1] else []
    output = []
    if node.tag == "figure":
        for child in list(node):
            if child.tag == "image":
                object = dict()
                object["type"] = "image"
                object["obj_counter"] = obj_counter + len(output)
                object["bbox"] = str_coords_to_tuple_coords(node.attrib["bbox"])
                if object["bbox"][0][0] <= full_slide_bbox[1][0] and object["bbox"][0][1] <= full_slide_bbox[1][1]:
                    output.append(object)
    for child in node:
        output += get_objects_from_element_tree(child, obj_counter + len(output), full_slide_bbox)
    return output


def get_objects_from_xml_file_path(file_path):
    with open(file_path, encoding="utf-8") as xml_file:
        tree = ElementTree.parse(xml_file)
    root = tree.getroot()
    objects = get_objects_from_element_tree(root, 0, None)
    object_id_to_objects = {object["obj_counter"]: object for object in objects}
    return object_id_to_objects


if __name__ == "__main__":
    with open("../../data/output/title-and-arrow-content-with-text-smart-art.xml", encoding="utf-8") as xml_file:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        elements = get_objects_from_element_tree(root, 0)
        for element in elements:
            print(element)
