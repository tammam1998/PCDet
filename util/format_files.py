from utils import *
from sys import argv
import os

DEFUALT_PATH = os.path.realpath(__file__).replace("/format_files.py", "")

def make_image_dir(to_path, filenames):
    """ takes a list of filenames and makes a sample image for each to match kitti format"""
    image_dir = os.path.join(to_path, "image_2")
    os.makedirs(image_dir)
    for f in filenames:
        image_file = os.path.join(image_dir, f + ".png")
        os.system("cp sample.png {}".format(image_file))

def make_calib_dir(to_path, filenames):
    """ takes a list of filenames and makes a fake calib for each to match kitti format"""
    calib_dir = os.path.join(to_path, "calib")
    os.makedirs(calib_dir)
    for f in filenames:
        calib_file = os.path.join(calib_dir, f + ".txt")
        os.system("cp calib.txt {}".format(calib_file))

def make_velo_dir(to_path, bin_files):
    """ takes a list of bin files and makes a copies them to match kitti format"""
    velo_dir = os.path.join(to_path, "velodyne")
    os.makedirs(velo_dir)
    for bin_file in bin_files:
        # calib_file = os.path.join(calib_dir, f + ".txt")
        # os.system("cp calib.txt {}".format(calib_file))
        _, name = os.path.split(bin_file)
        velo_file = os.path.join(velo_dir, name)
        os.system("cp {} {}".format(bin_file, velo_file))

def create_image_set(to_path, filenames):
    set_dir = os.path.join(to_path, "ImageSets")
    os.makedirs(set_dir)
    test_file = os.path.join(set_dir, "test.txt")
    with open(test_file, "w") as f:
        for name in sorted(filenames):
            f.write(str(name) +"\n")
    train_file = os.path.join(set_dir, "train.txt")
    f = open(train_file, "w")

    val_file = os.path.join(set_dir, "val.txt")
    f = open(val_file, "w")


def main(from_path, to_path, split="testing"):
    filenames = [f.replace(".bin", "") for f in os.listdir(from_path) if f.endswith(".bin")]
    bin_files = [os.path.join(from_path, f) for f in os.listdir(from_path) if f.endswith(".bin")]

    create_image_set(to_path, filenames)

    if split == "testing":
        to_path = os.path.join(to_path, "testing")
    else:
        to_path = os.path.join(to_path, "training")

    make_image_dir(to_path, filenames)
    make_calib_dir(to_path, filenames)
    make_velo_dir(to_path, bin_files)
    
if __name__ == "__main__":
    """takes path as argument"""
    if len(argv) > 1:
        from_path = argv[1]
        to_path = os.path.join(DEFUALT_PATH, "data/kitti") if len(argv)==2  else argv[2]
        os.system("rm -r {}".format(to_path))
    else:
        raise Exception("please incluude from_dir and to_dir in args")

    main(from_path, to_path)