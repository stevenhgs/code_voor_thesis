import math

import cv2
import numpy as np
import matplotlib.pyplot as plt


resizing_size = (750, 750)


def preprocess_image(img):
    # preprocessed_image = cv2.resize(img, resizing_size)
    preprocessed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    preprocessed_image = cv2.GaussianBlur(preprocessed_image, (15, 15), 1)
    preprocessed_image = cv2.Canny(preprocessed_image, 50, 50)
    preprocessed_image = cv2.dilate(preprocessed_image, np.ones((3, 3)), iterations=2)
    preprocessed_image = cv2.erode(preprocessed_image, np.ones((2, 2)), iterations=4)
    cv2.imshow("a", preprocessed_image)
    cv2.waitKey(0)
    return preprocessed_image


def find_tip_of_arrow(points, indices_on_convex_hull):
    nb_points = len(points)
    indices_of_points_not_on_convex_hull = []
    convex_hull_indices_set = set(indices_on_convex_hull)
    for i in range(nb_points):
        if i not in convex_hull_indices_set:
            indices_of_points_not_on_convex_hull.append(i)

    index_not_on_convex_hull1, index_not_on_convex_hull2 = indices_of_points_not_on_convex_hull
    if np.all(points[(index_not_on_convex_hull1 + 2) % nb_points] == points[(index_not_on_convex_hull2 - 2) % nb_points]):
        return tuple(points[(index_not_on_convex_hull1 + 2) % nb_points]), points[index_not_on_convex_hull1], points[index_not_on_convex_hull2]
    if np.all(points[(index_not_on_convex_hull2 + 2) % nb_points] == points[(index_not_on_convex_hull1 - 2) % nb_points]):
        return tuple(points[(index_not_on_convex_hull2 + 2) % nb_points]), points[index_not_on_convex_hull1], points[index_not_on_convex_hull2]
    return None, None, None


def find_base_of_arrow(points, tip_of_arrow):
    nb_points = len(points)
    for i in range(nb_points):
        if tip_of_arrow[0] == points[i][0] and tip_of_arrow[1] == points[i][1]:
            p1, p2 = tuple(points[(i + 3) % nb_points]), tuple(points[(i - 3) % nb_points])
            return tuple([(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2])


def constraint_on_cycles(polygon):
    seen_points = set()
    for i in range(len(polygon)):
        point = (polygon[i][0][0], polygon[i][0][1])
        if point in seen_points:
            # print(seen_points)
            return False
        seen_points.add(point)
    # print(seen_points)
    return True


def get_distance_between_two_points(p1, p2):
    x_diff = p1[0] - p2[0]
    y_diff = p1[1] - p2[1]
    return math.sqrt(x_diff * x_diff + y_diff * y_diff)


def constraint_on_tip_of_arrow(tip_of_arrow, non_convex_hull_point1, non_convex_hull_point2):
    dist1 = get_distance_between_two_points(tip_of_arrow, non_convex_hull_point1)
    dist2 = get_distance_between_two_points(tip_of_arrow, non_convex_hull_point2)
    if dist1 == 0 or dist2 == 0:
        return False
    # print(f'{dist1=}, {dist2=}, {dist1/dist2=}')
    lower_bound = dist1 * 0.85
    upper_bound = dist1 * 1.15
    return lower_bound <= get_distance_between_two_points(tip_of_arrow, non_convex_hull_point2) <= upper_bound


def get_approximated_polygon_layered(contours, epsilons):
    """
    The lower epsilon the more points will be in the approximation.
    """
    approximated_polygon = contours
    for epsilon in epsilons:
        perimeter = cv2.arcLength(approximated_polygon, closed=True)
        approximated_polygon = cv2.approxPolyDP(approximated_polygon, epsilon * perimeter, True)
    return approximated_polygon


def plot_contour(contour):
    for i in range(len(contour) - 1):
        plt.plot([contour[i][0][0], contour[i + 1][0][0]], [contour[i][0][1], contour[i + 1][0][1]], 'bo-')
    plt.plot([contour[-1][0][0], contour[0][0][0]], [contour[-1][0][1], contour[0][0][1]], 'bo-')
    plt.show()


def plot_contour_and_convex_hull(contour, indices_on_convex_hull):
    for i in range(len(contour) - 1):
        plt.plot([contour[i][0][0], contour[i + 1][0][0]], [contour[i][0][1], contour[i + 1][0][1]], 'bo-')
    plt.plot([contour[-1][0][0], contour[0][0][0]], [contour[-1][0][1], contour[0][0][1]], 'bo-')

    for i in range(len(indices_on_convex_hull) - 1):
        plt.plot([contour[indices_on_convex_hull[i][0]][0][0], contour[indices_on_convex_hull[i + 1][0]][0][0]], [contour[indices_on_convex_hull[i][0]][0][1], contour[indices_on_convex_hull[i + 1][0]][0][1]], 'ro-')
    plt.plot([contour[indices_on_convex_hull[-1][0]][0][0], contour[indices_on_convex_hull[0][0]][0][0]], [contour[indices_on_convex_hull[-1][0]][0][1], contour[indices_on_convex_hull[0][0]][0][1]], 'ro-')
    plt.show()


def find_arrows_in_image(image_path, view=False):
    """
    This method is only used in experiments.
    """
    image = cv2.imread(image_path)
    # resized_image = cv2.resize(image, resizing_size)
    resized_image = image
    preprocessed_image = preprocess_image(image)
    contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    nb_arrows_detected = 0

    for contour in contours:
        approximated_polygon = get_approximated_polygon_layered(contour, [0.005, 0.022])
        print('aaaa')
        print(approximated_polygon)
        print(type(approximated_polygon))
        indices_on_convex_hull = cv2.convexHull(approximated_polygon, returnPoints=False)
        print(indices_on_convex_hull)
        nb_sides_of_convex_hull = len(indices_on_convex_hull)

        if 6 > nb_sides_of_convex_hull > 3 and nb_sides_of_convex_hull + 2 == len(approximated_polygon):
            tip_of_arrow, p1, p2 = find_tip_of_arrow(approximated_polygon[:, 0, :], indices_on_convex_hull.squeeze())
            # print(p1, p2)
            if tip_of_arrow is not None and constraint_on_tip_of_arrow(tip_of_arrow, p1, p2) and constraint_on_cycles(approximated_polygon):
                nb_arrows_detected += 1
                cv2.drawContours(resized_image, [contour], -1, (200, 0, 255), 3)
                cv2.circle(resized_image, tip_of_arrow, 3, (0, 255, 0), cv2.FILLED)
                # print(tip_of_arrow)
                plot_contour(contour)
                plot_contour(approximated_polygon)
                plot_contour_and_convex_hull(approximated_polygon, indices_on_convex_hull)

    if view:
        cv2.imshow("Image", resized_image)
        cv2.waitKey(0)
    return nb_arrows_detected


def find_arrow_from_list_of_points2(points):
    """
    Finds it based on the order of the points.
    Not always correct.
    """
    if len(points) != 7:
        return None, None

    all_possible_combinations = []
    def dfs(current, unused):
        if len(current) == 7:
            all_possible_combinations.append(current)
            return
        for i in unused:
            new_unused = set(unused)
            new_unused.remove(i)
            dfs(current + [points[i]], new_unused)
    dfs([points[0]], {i+1 for i in range(6)})
    for points in all_possible_combinations:
        np_points = np.array([[[x, y]] for x, y in points]).astype(np.float32)

        indices_on_convex_hull = cv2.convexHull(np_points, returnPoints=False)
        tip_of_arrow, p1, p2 = find_tip_of_arrow(np_points[:, 0, :], indices_on_convex_hull.squeeze())
        if tip_of_arrow is None:
            continue
        base_of_arrow = find_base_of_arrow(np_points[:, 0, :], tip_of_arrow)
        return tip_of_arrow, base_of_arrow


def find_arrow_from_list_of_points(points):
    """
    Finds it geometrically.
    """
    if len(points) != 7:
        return None, None
    np_points = np.array([[[x, y]] for x, y in points]).astype(np.float32)

    indices_on_convex_hull = cv2.convexHull(np_points, returnPoints=False)
    # expect two points not on convex_hull for arrow
    if len(indices_on_convex_hull) != 5:
        return None, None
    tip_of_arrow, base_of_arrow = find_tip_and_base_of_arrow_geometrically(np_points[:, 0, :], indices_on_convex_hull.squeeze())
    return tip_of_arrow, base_of_arrow


def find_tip_and_base_of_arrow_geometrically(points, indices_on_convex_hull):
    p1_not_on_convex_hull, p2_not_on_convex_hull = None, None
    for i in range(len(points)):
        if i not in indices_on_convex_hull:
            if p1_not_on_convex_hull is None:
                p1_not_on_convex_hull = points[i]
            elif p2_not_on_convex_hull is None:
                p2_not_on_convex_hull = points[i]
                break
    if p2_not_on_convex_hull is None:
        return None, None
    p1x, p1y = p1_not_on_convex_hull
    p2x, p2y = p2_not_on_convex_hull
    if p1x == p2x:
        p2x += 0.000001
    # slope of line between p1 and p2
    # m = (y2-y1)/(x2-x1)
    slope = (p2y - p1y) / (p2x - p1x)
    # point between p1 and p2
    midx = (p1x + p2x) / 2
    midy = (p1y + p2y) / 2
    # equation of line through mid point and perpendicular to slope (y-y3)/(x-x3) = -1/m
    # x = (y3-y)*m + x3
    # x = m*y3 - m*y + x3
    # x + m*y - (m*y3 + x3) = 0
    # a = 1, b = m, c = -(m*y3 + x3)
    # ax + by + c = 0
    a = 1
    b = slope
    c = -(slope * midy + midx)
    closest_distance = math.inf
    tip_of_arrow = None
    for index in indices_on_convex_hull:
        px, py = points[index]
        distance = abs(a * px + b * py + c) / math.sqrt(a**2 + b**2)
        if distance < closest_distance:
            tip_of_arrow = (px, py)
            closest_distance = distance
    # equation of line through p1 and p2
    # y = mx + c
    # mx - y + c = 0
    # ax + by + c = 0
    # c = y - mx
    a = slope
    b = -1
    c = p1y - slope * p1x

    furthest_distance1 = -math.inf
    furthest_distance2 = -math.inf
    base_of_arrow1 = None
    base_of_arrow2 = None
    for index in indices_on_convex_hull:
        px, py = points[index]
        if px == tip_of_arrow[0] and py == tip_of_arrow[1]:
            continue
        distance = abs(a * px + b * py + c) / math.sqrt(a ** 2 + b ** 2)
        if distance > furthest_distance1:
            base_of_arrow2 = base_of_arrow1
            furthest_distance2 = furthest_distance1
            base_of_arrow1 = (px, py)
            furthest_distance1 = distance
        elif distance > furthest_distance2:
            base_of_arrow2 = (px, py)
            furthest_distance2 = distance

    base_of_arrow = ((base_of_arrow1[0] + base_of_arrow2[0]) / 2, (base_of_arrow1[1] + base_of_arrow2[1]) / 2)
    return tip_of_arrow, base_of_arrow








if __name__ == "__main__":
    print(find_arrow_from_list_of_points2([(621.040,256.120),(651.470,243.410),(656.080,254.440),(672.150,215.330),(633.040,199.260),(637.650,210.300),(607.210,223.010)]))
