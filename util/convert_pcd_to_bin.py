import numpy as np
import os
import struct
from os.path import isfile, join
from sys import argv
from pypcd import pypcd
from utils import draw_lidar_simple, load_velo_scan, extract_array_from_pcd_obj

DEFUALT_PATH = os.path.realpath(__file__).replace("/convert_pcd_to_bin.py", "")



def main(path):
    pcd_filenames = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".pcd")]
    # draw_lidar_simple(data)
    for pcd_file in pcd_filenames:
        pcd = pypcd.PointCloud.from_path(pcd_file)
        data = extract_array_from_pcd_obj(pcd)
        bin_file = pcd_file.replace(".pcd", ".bin")
        print(bin_file)
        data.tofile(bin_file)



if __name__ == "__main__":
    """takes path as argument"""
    if len(argv) > 1:
        path = argv[1]
    else:
        path = DEFUALT_PATH
    main(path)