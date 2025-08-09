import matplotlib.pyplot as plt


def get_shape_compositions(file_name):
    file = open(file_name)
    file_data = file.read()
    file_lines = file_data.split('\n')
    nb_lines = len(file_lines)
    i = 0
    shape_compositions = []

    while i < nb_lines:
        line = file_lines[i]

        if line.split(' ')[0] == "<rect":
            i += 1
            coords_of_shapes = []

            while i < nb_lines and file_lines[i].split(" ")[0] == "<curve":
                points = file_lines[i].split("pts=")[-1][1:-3]
                shape_coords = [[], []]
                for j, point in enumerate(points.split(',')):
                    shape_coords[j % 2].append(float(point))
                coords_of_shapes.append(shape_coords)
                i += 1

            if len(coords_of_shapes) > 0:
                shape_compositions.append(coords_of_shapes)
        i += 1

    return shape_compositions


def plot_shape_compositions(plot_shape_compositions):
    for shape_composition in plot_shape_compositions:
        for shape in shape_composition:
            nb_points = len(shape[0])
            for i in range(nb_points):
                next_index = (i + 1) % nb_points
                plt.plot([shape[0][i], shape[0][next_index]], [shape[1][i], shape[1][next_index]], 'r-')
        plt.show()


def plot_slide(file_name):
    shape_compositions = get_shape_compositions(file_name)
    plot_shape_compositions(shape_compositions)


file_path = "../../complete_pipeline/xmls/dummy_0.xml"
plot_slide(file_path)
