
from utils import load_velo_scan
from pypcd import pypcd
import os
from sys import argv

DEFUALT_PATH = os.path.realpath(__file__).replace("/adjust.py", "")


def main(from_path, to_path):
    only_lidar_files = [os.path.join(from_path, f) for f in os.listdir(from_path) if f.endswith(".bin")]
    offset = +0.225 #decrease z axis by this amount
    for lidar_file in only_lidar_files:
        pcd = load_velo_scan(lidar_file)
        # print(pcd[:3, :])
        pcd[:,2] += offset
        # pcd[:,3] /= 255
        # print(pcd[:3, :])
        pcd.tofile(lidar_file)

if __name__ == "__main__":
    """takes path as argument"""
    if len(argv) > 1:
        from_path = argv[1]
        to_path = os.path.join(DEFUALT_PATH, "data/kitti") if len(argv)==2  else argv[2]
    else:
        raise Exception("please incluude from_dir and to_dir in args")

    main(from_path, to_path)