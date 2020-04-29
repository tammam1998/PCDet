import pickle
from sys import argv
import utils
import os
import numpy as np



DEFUALT_PATH = os.path.realpath(__file__).replace("/read_output.py", "")


def rotate(theta, point):
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return rotation_matrix.dot(point)

def make_points(lidar):
    x, y, z, w, l, h, rz = lidar[0], lidar[1], lidar[2], lidar[3], lidar[4], lidar[5], lidar[6]
    origin = [[x],[y],[z]]
    point1 = np.array([[l/2], [w/2], [h/2]])
    point2 = np.array([[l/2], [-w/2], [h/2]])
    point3 = np.array([[-l/2], [w/2], [h/2]])
    point4 = np.array([[-l/2], [-w/2], [h/2]])
    point5 = np.array([[l/2], [w/2], [-h/2]])
    point6 = np.array([[l/2], [-w/2], [-h/2]])
    point7 = np.array([[-l/2], [w/2], [-h/2]])
    point8 = np.array([[-l/2], [-w/2], [-h/2]])
    points = [point1, point2, point3, point4, point5, point6, point7, point8]

    for idx in range(len(points)):
        point = points[idx] + origin
        point = rotate(rz, point)
        points[idx] = point

    return np.array(points).reshape(-1, 3)

def main(from_path, to_path):
    annos = pickle.load(open(from_path, "rb"))
    bbox = annos[0]["boxes_lidar"][0]
    points = make_points(bbox)
    utils.draw_cube(points)
    input_str = input()
    if input_str == "killall":
        return




if __name__ == "__main__":
    """takes path as argument"""
    if len(argv) > 1:
        from_path = argv[1]
        to_path = os.path.join(DEFUALT_PATH, "data/kitti") if len(argv)==2  else argv[2]
    else:
        raise Exception("please incluude from_dir and to_dir in args")

    main(from_path, to_path)