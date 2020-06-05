import numpy as np
from mayavi import mlab
import struct
def load_velo_scan(velo_filename, dtype=np.float32, n_vec=4):
    scan = np.fromfile(velo_filename, dtype=dtype)
    scan = scan.reshape((-1, n_vec))
    return scan


def draw_lidar_simple(pc, color=None):
    ''' Draw lidar points. simplest set up. '''
    fig = mlab.figure(bgcolor=(0,0,0), size=(640, 360))
    if color is None: color = pc[:, 2]
    #draw points
    mlab.points3d(pc[:,0], pc[:,1], pc[:,2], color,color=None, mode='point', colormap = 'gnuplot', scale_factor=1, figure=fig)
    # draw origin
    mlab.points3d(0, 0, 0, color=(1,1,1), mode='sphere', scale_factor=0.2)
    #draw axis
    axes=np.array([
        [2.,0.,0.,0.],
        [0.,2.,0.,0.],
        [0.,0.,2.,0.],
    ],dtype=np.float64)
    mlab.plot3d([0, axes[0,0]], [0, axes[0,1]], [0, axes[0,2]], color=(1,0,0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[1,0]], [0, axes[1,1]], [0, axes[1,2]], color=(0,1,0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[2,0]], [0, axes[2,1]], [0, axes[2,2]], color=(0,0,1), tube_radius=None, figure=fig)
    mlab.view(azimuth=180, elevation=70, focalpoint=[ 12.0909996 , -1.04700089, -2.03249991], distance=62.0, figure=fig)
    mlab.show()
    return fig


def convert_bin_to_pcd(binFilePath):
    list_pcd = load_velo_scan(binFilePath)[:, :3]
    np_pcd = np.asarray(list_pcd)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd)
    return pcd


def viz_bin_file(velo_filename, n_vec=4):
    pcd = load_velo_scan(velo_filename, n_vec=n_vec)
    pcd = pcd[:, 0:n_vec]
    draw_lidar_simple(pcd)

    # mlab.clf()
    input_str = input()
    if input_str == "killall":
        return

def extract_array_from_pcd_obj(pcd):
    """ return [x, y, z, intensity] array"""
    x = np.array(pcd.pc_data["x"]).reshape(-1, 1)
    y = np.array(pcd.pc_data["y"]).reshape(-1, 1)
    z = np.array(pcd.pc_data["z"]).reshape(-1, 1)
    intensity = np.array(pcd.pc_data["intensity"]).reshape(-1, 1)
    data = np.hstack([x, y, z, intensity])
    return data