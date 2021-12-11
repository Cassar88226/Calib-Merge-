import cv2
import numpy as np

cap1 = cv2.VideoCapture('1.ts')
cap2 = cv2.VideoCapture('2.ts')
cap3 = cv2.VideoCapture('3.ts')
cap4 = cv2.VideoCapture('4.ts')
counts = []
total1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
total2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
total3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))
total4 = int(cap4.get(cv2.CAP_PROP_FRAME_COUNT))
cnt = 0
vid_writer = cv2.VideoWriter("output.ts", cv2.VideoWriter_fourcc(*"mp4v"), 25, (5824, 3072))
if cap2.isOpened():
    for i in range(34):
        ret2, frame2 = cap2.read()
total2 = total2 - 34
counts = []
counts.append(total1)
counts.append(total2)
counts.append(total3)
counts.append(total4)
minCount = min(counts)
cnt = 0
if cap1.isOpened() and cap2.isOpened() and cap3.isOpened() and cap4.isOpened():
    while(cnt < minCount):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        ret3, frame3 = cap3.read()
        ret4, frame4 = cap4.read()
        if ret1 == True and ret2 == True and ret3 == True and ret4 == True:
           
            split1 = frame1[0:,0:1375]
            split2 = frame3[0:,0:1360]
            vis1 = np.concatenate((split1, frame2), axis=1)
            vis2 = np.concatenate((split2, frame4), axis=1)
            split3 = vis1[0:,0:2736]
            vis3 = np.concatenate((split3, vis2), axis=1)
            vid_writer.write(vis3)
        cnt += 1
        print(cnt)
vid_writer.release()

