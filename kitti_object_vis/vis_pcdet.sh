cp -r ../data/kitti/testing/velodyne/* data/object/training/velodyne/

cp -r ../output/second/default/eval/epoch_no_number/test/default/final_result/data/* data/object/training/label_2/

# cp -r ../output/PartA2_fc/default/eval/epoch_2/test/default/final_result/data/* data/object/training/label_2/

python kitti_object.py --show_lidar_with_depth --img_fov --const_box --vis --ind 10