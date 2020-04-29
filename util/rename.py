import os
from os.path import isfile, join
from sys import argv

DEFUALT_PATH = os.path.realpath(__file__).replace("/rename.py", "")

def main(path):
    print(path)
    only_lidar_files = [join(path, f) for f in os.listdir(path) if f.endswith(".pcd")]
    
    for data_idx, src_path in enumerate(only_lidar_files):
        to_path = join(path, "%010d.pcd" % (data_idx))
        os.rename(src_path, to_path)

if __name__ == "__main__":
    if len(argv) > 1:
        path = argv[1]
    else:
        path = DEFUALT_PATH
    main(path)