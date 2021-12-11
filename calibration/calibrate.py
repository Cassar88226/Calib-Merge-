import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import scipy.io
import pickle
import os

def getCams(configdir):

    cams = []
    for i in range(4):
        cam_filepath = os.path.join(configdir, 'camera%02d' % (i + 1), 'calibration.mat')
        cam_np = scipy.io.loadmat(cam_filepath)['cam']
        cam_dict = {}
        for key in cam_np.dtype.fields.keys():  # ['K', 'R', 'fc', 'cc', 'alpha_c', 'kc', 'T', 'P', 'H', ]
            cam_dict[key] = cam_np[key][0][0]
        cam_dict['fc'] = cam_dict['fc'].flatten()
        cam_dict['kc'] = cam_dict['kc'].flatten()
        cam_dict['cc'] = cam_dict['cc'].flatten()
        cams.append(cam_dict)
    return cams
''''
The focal length and the camera center are the camera intrinsic parameters, K. (K is an industry norm to express the intrinsic matrix.)

'''
def main(configdir):

    cams = getCams(configdir)
    # print(cams[0])
    cameraMatrix1 = cams[1]['K']
    distCoeff1 = cams[1]['kc']
    rvecs1 = cams[1]['R']
    tvecs1 = cams[1]['R']
    img1 = cv2.imread("image/1.jpg")
    h,  w = img1.shape[:2]
    alpha_c1 = cams[1]['alpha_c']
    newCameraMatrix1, roi1 = cv2.getOptimalNewCameraMatrix(cameraMatrix1, distCoeff1, (w,h), int(alpha_c1), (w,h))
    dst = cv2.undistort(img1, cameraMatrix1, distCoeff1, None, newCameraMatrix1)
    x, y, w, h = roi1
    cv2.imwrite('caliResult1_1.png', dst)
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite('calibResult1_2.png', dst)

    cameraMatrix2 = cams[2]['K']
    distCoeff2 = cams[2]['kc']
    rvecs2 = cams[2]['R']
    tvecs2 = cams[2]['R']
    img2 = cv2.imread("image/2.jpg")
    h,  w = img2.shape[:2]
    alpha_c2 = cams[2]['alpha_c']
    newCameraMatrix2, roi2 = cv2.getOptimalNewCameraMatrix(cameraMatrix2, distCoeff2, (w,h), int(alpha_c2), (w,h))
    dst = cv2.undistort(img2, cameraMatrix2, distCoeff2, None, newCameraMatrix2)
    x, y, w, h = roi2
    cv2.imwrite('caliResult2_1.png', dst)
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite('calibResult2_2.png', dst)
    print(cameraMatrix2)
    # with open(os.path.join(configdir,'calibration.pckl'), 'wb') as f:
    #     pickle.dump(cams, f)
    # cap1 = cv2.VideoCapture('1.ts')
    # cap2 = cv2.VideoCapture('2.ts')
    # cap3 = cv2.VideoCapture('3.ts')
    # cap4 = cv2.VideoCapture('4.ts')
    # while(cap1.isOpened() and cap2.isOpened()):
    #     ret1, frame1 = cap1.read()
    #     ret2, frame2 = cap2.read()
    #     ret3, frame3 = cap3.read()
    #     ret4, frame4 = cap4.read()
    #     if ret1 == True and ret2 == True:
    #         # cv2.imwrite("1.png",frame1)
    #         # cv2.imwrite("2.png",frame2)
    #         # cv2.imwrite("3.png",frame3)
    #         # cv2.imwrite("4.png",frame4)
    #         split1 = frame1[0:,0:1375]
    #         split2 = frame3[0:,0:1360]
    #         vis1 = np.concatenate((split1, frame2), axis=1)
    #         vis2 = np.concatenate((split2, frame4), axis=1)
    #         vis3 = np.concatenate((vis1, vis2), axis=1)
    #         cv2.imwrite("result1.png",vis1)
    #         cv2.imwrite("result2.png",vis2)
    #         cv2.imwrite("result.png",vis3)
    #         cv2.imshow('Frame',vis1)
    #         cv2.waitKey(0)
# @click.command()
# @click.option('--configdir', help='Path to the config directory of the relevant msr-file.')
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    configdir = filedialog.askdirectory()
    main(configdir)
