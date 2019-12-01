import cv2
import numpy
vidcap = cv2.VideoCapture('NYC VIDEO FINAL H264.mp4')
success,image=vidcap.read()
# print('Read a new frame: ',success)
cv2.imwrite("frame%d.jpg" % 1, image)
count=1
while success:
     success,image=vidcap.read()
     if success:
          cv2.imwrite("frame%d.jpg" % count,image)
     count+=1



