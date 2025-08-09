from xml_to_objects import get_objects_from_xml_file_path
from matplotlib import pyplot as plt

if __name__ == "__main__":
    object_id_to_object = get_objects_from_xml_file_path("../../data/output/title-and-arrow-content-with-text-smart-art.xml")
    ax = plt.gca()
    ax.set_xlim([0, 960])
    ax.set_ylim([0, 540])
    for object_id, object in object_id_to_object.items():
        if object["type"] == "curve":
            print(len(object["pts"]))
            points = object["pts"]
            nb_points = len(points)
            for i in range(nb_points):
                next_index = (i + 1) % nb_points
                plt.plot([points[i][0], points[next_index][0]], [points[i][1], points[next_index][1]], 'b-')
    plt.show()

