import numpy as np
import os
from mayavi import mlab
from pypcd import pypcd
from utils import  *

DEFUALT_PATH = os.path.realpath(__file__).replace("/vis.py", "")


def main():
    only_lidar_files = [os.path.join(DEFUALT_PATH, f) for f in os.listdir(DEFUALT_PATH) if f.endswith(".bin")]
    file_path = "/home/tammam/ml_urop/data/0000000114.bin"
    
    pcd = load_velo_scan(file_path)
    # pcd = pypcd.PointCloud.from_path(file_path) # Read the point cloud
    # cloud = o3d.geometry.PointCloud()
    # cloud.points = o3d.utility.Vector3dVector(pcd)
    # # pcd = convert_kitti_bin_to_pcd(file_path)
    # o3d.visualization.draw_geometries([cloud])
    # x = np.array(pcd.pc_data["x"]).reshape(-1, 1)
    # y = np.array(pcd.pc_data["y"]).reshape(-1, 1)
    # z = np.array(pcd.pc_data["z"]).reshape(-1, 1)
    # print(pcd.pc_data["x"].min(), np.max(y), np.mean(z))
    # pcd = np.hstack([x, y, z])
    
    draw_lidar_simple(pcd)

    # mlab.clf()
    input_str = input()
    if input_str == "killall":
        return

if __name__ == "__main__":
    main()