import fitz
from collections import defaultdict
from src.xml_parsing.xml_to_objects import get_objects_from_xml_file_path
from src.base_predicates.base_predicates import get_base_predicates_from_objects


def draw_object_ids_on_pdfs(pdf_input_directory_path, xml_input_directory_path, output_path, file_name):
    PDF_HEIGHT = 540
    TEXT_PADDING = 5
    TEXT_SIZE = 45
    type_to_color = {
        "Text": (1, 0, 0),
        "Shape": (0, 1, 0),
        "Image": (1, 0, 1),
        "Arrow": (0, 0, 1)
    }
    pdf_input_path = f"{pdf_input_directory_path}{file_name}.pdf"
    xml_input_path = f"{xml_input_directory_path}{file_name}.xml"
    object_id_to_object = get_objects_from_xml_file_path(xml_input_path)

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
    relations = get_base_predicates_from_objects(object_id_to_object)

    # add name for presentation
    counters = defaultdict(lambda: 1)
    for key in list(object_id_to_object):
        object = object_id_to_object[key]
        object["object_id"] = "Obj_" + str(key)
        if object["type"] == "Text":
            object["name"] = "Text"
            object["object_name"] = "Text"
        elif object["type"] == "image":
            object["name"] = "Image"
            object["object_name"] = "Image"
        else:
            if object["obj_counter"] in relations["Arrow"]:
                object["name"] = "Arrow"
            else:
                object["name"] = "Shape"
            object["object_name"] = "Shape"
        object["counter"] = counters[object["name"]]
        counters[object["name"]] += 1

    for key, val in relations.items():
        print(f'{key}: {val}')

    # base predicates
    # open pdf for fitz
    doc = fitz.open(pdf_input_path)
    page = doc[0]

    for object_id, object in object_id_to_object.items():
        text_size = TEXT_SIZE
        if object["name"] == "Arrow":
            for id, (x, y) in relations["TipOfArrow"]:
                if id == object_id:
                    page.draw_circle((x, PDF_HEIGHT - y), 5, color=(0.5, 0.1, 0.1), width=2)
            for id, (x, y) in relations["BaseOfArrow"]:
                if id == object_id:
                    page.draw_circle((x, PDF_HEIGHT - y), 5, color=(0.1, 0.5, 0.1), width=2)

        color = type_to_color[object["name"]]
        lower_left, upper_right = object["bbox"]
        rectangle_position = [lower_left[0], PDF_HEIGHT - upper_right[1], upper_right[0], PDF_HEIGHT - lower_left[1]]
        page.draw_rect(rectangle_position, color=color, width=2)
        text_point = fitz.Point(lower_left[0], PDF_HEIGHT - upper_right[1] - TEXT_PADDING)
        if object["name"] == "Image":
            text_point = fitz.Point(lower_left[0], PDF_HEIGHT - lower_left[1] + TEXT_SIZE)
        elif object["name"] == "Arrow" and object["counter"] == 1:
            text_point = fitz.Point(lower_left[0] - 63, PDF_HEIGHT - upper_right[1] - TEXT_PADDING)
        elif object["name"] == "Arrow" and object["counter"] == 2:
            text_point = fitz.Point(lower_left[0], PDF_HEIGHT - upper_right[1] - TEXT_PADDING - 10)
        page.insert_text(text_point,  # bottom-left of 1st char
                         object["object_id"],  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=text_size,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         color=color)

        for (_, _), ((x1, y1), (x2, y2)) in relations["AtTipOfArrow"]:
            page.draw_line((x1, PDF_HEIGHT - y1), (x2, PDF_HEIGHT - y2), color=(0.5, 0.1, 0.1), width=2)

        for (_, _), ((x1, y1), (x2, y2)) in relations["AtBaseOfArrow"]:
            page.draw_line((x1, PDF_HEIGHT - y1), (x2, PDF_HEIGHT - y2), color=(0.1, 0.5, 0.1), width=2)

    doc.save(f'{output_path}{file_name}.pdf')


def draw_object_ids_on_pdfs_multiple_pages(pdf_input_directory_path, xml_input_directory_path, output_path, file_name, nb_pages):
    # get this from XML
    PDF_HEIGHT = 540
    # PDF_HEIGHT = 405
    # PDF_HEIGHT = 255.118
    TEXT_PADDING = 5
    TEXT_SIZE = PDF_HEIGHT // 28
    type_to_color = {
        "Text": (1, 0, 0),
        "Shape": (0, 1, 0),
        "Image": (1, 0, 1),
        "Arrow": (0, 0, 1)
    }
    pdf_input_path = f"{pdf_input_directory_path}{file_name}.pdf"
    doc = fitz.open(pdf_input_path)
    for i in range(nb_pages):
        page = doc[i]
        xml_input_path = f"{xml_input_directory_path}{file_name}_{i}.xml"
        object_id_to_object = get_objects_from_xml_file_path(xml_input_path)

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
        relations = get_base_predicates_from_objects(object_id_to_object)

        # add name for presentation
        counters = defaultdict(lambda: 1)
        for key in list(object_id_to_object):
            object = object_id_to_object[key]
            object["object_id"] = "Obj_" + str(key)
            if object["type"] == "Text":
                object["name"] = "Text"
                object["object_name"] = "Text"
            elif object["type"] == "image":
                object["name"] = "Image"
                object["object_name"] = "Image"
            else:
                if object["obj_counter"] in relations["Arrow"]:
                    object["name"] = "Arrow"
                else:
                    object["name"] = "Shape"
                object["object_name"] = "Shape"
            object["counter"] = counters[object["name"]]
            counters[object["name"]] += 1

        print(f'PAGE {i}:')
        for key, val in relations.items():
            print(f'{key}: {val}')
        print()

        for object_id, object in object_id_to_object.items():
            text_size = TEXT_SIZE
            if object["name"] == "Arrow":
                for id, (x, y) in relations["TipOfArrow"]:
                    if id == object_id:
                        page.draw_circle((x, PDF_HEIGHT - y), 5, color=(0.5, 0.1, 0.1), width=2)
                for id, (x, y) in relations["BaseOfArrow"]:
                    if id == object_id:
                        page.draw_circle((x, PDF_HEIGHT - y), 5, color=(0.1, 0.5, 0.1), width=2)

            color = type_to_color[object["name"]]
            lower_left, upper_right = object["bbox"]
            rectangle_position = [lower_left[0], PDF_HEIGHT - upper_right[1], upper_right[0], PDF_HEIGHT - lower_left[1]]


            # + is up - is down
            page.draw_rect(rectangle_position, color=color, width=1)
            text_point = fitz.Point(lower_left[0] + 2, PDF_HEIGHT - upper_right[1] + TEXT_PADDING)
            if object["name"] == "Image":
                text_point = fitz.Point(lower_left[0] + 10, PDF_HEIGHT - upper_right[1] + 10 + TEXT_PADDING)
            elif object["name"] == "Arrow" and object["counter"] == 1:
                text_point = fitz.Point(lower_left[0] - 12, PDF_HEIGHT - upper_right[1] - TEXT_PADDING)
            elif object["name"] == "Arrow" and object["counter"] == 2:
                text_point = fitz.Point(lower_left[0], PDF_HEIGHT - upper_right[1] - TEXT_PADDING - 10)
            elif object["name"] == "Text" and relations.get("InBulletPoint") is not None and (object_id,) in relations["InBulletPoint"]:
                color = (0, 0.5, 1)
            elif object["name"] == "Text" and relations.get("InEnumeration") is not None and (object_id,) in relations["InEnumeration"]:
                color = (0.2, 0.5, 0.2)
            elif object["name"] == "Shape":
                text_point = fitz.Point(lower_left[0] + 1, PDF_HEIGHT - upper_right[1] - TEXT_PADDING)
            page.insert_text(text_point,  # bottom-left of 1st char
                             object["object_id"][4:],  # the text (honors '\n')
                             fontname="helv",  # the default font
                             fontsize=text_size,  # the default font size
                             rotate=0,  # also available: 90, 180, 270
                             color=color)

            for (_, _), ((x1, y1), (x2, y2)) in relations["AtTipOfArrow"]:
                page.draw_line((x1, PDF_HEIGHT - y1), (x2, PDF_HEIGHT - y2), color=(0.5, 0.1, 0.1), width=2)

            for (_, _), ((x1, y1), (x2, y2)) in relations["AtBaseOfArrow"]:
                page.draw_line((x1, PDF_HEIGHT - y1), (x2, PDF_HEIGHT - y2), color=(0.1, 0.5, 0.1), width=2)

        page.insert_text(fitz.Point(0, 20),  # bottom-left of 1st char
                         str(len(object_id_to_object.items())),  # the text (honors '\n')
                         fontname="helv",  # the default font
                         fontsize=20,  # the default font size
                         rotate=0,  # also available: 90, 180, 270
                         color=(0.5, 0.5, 0.1))

    doc.save(f'{output_path}{file_name}.pdf')


if __name__ == "__main__":
    pdf_input_directory_path = "../../data/input/"
    xml_input_directory_path = "../../data/output/"
    output_path = "../../complete_pipeline/object_id_on_pdf/"
    file_names = ["bullet_points"]
    for file_name in file_names:
        draw_object_ids_on_pdfs(pdf_input_directory_path, xml_input_directory_path, output_path, file_name)
