#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 9:30
# @Author : skl
# @File   : redpoint.py
import cv2
import numpy as np



def readimage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hue_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_range = np.array([0, 100, 80])
    high_range = np.array([5, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)

    dilated = cv2.dilate(
        th, cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (2, 2)), iterations=2)
    circles = cv2.HoughCircles(
    # dp：累加器分辨率与图像分辨率的反比。dp获取越大，累加器数组越小。
    # minDist：圆心最小距离。
    # param1：边缘检测的梯度。
    # param2：累加器阈值，越小圈子越多。
        dilated,
        cv2.HOUGH_GRADIENT,
        0.8,
        70,
        param1=50,
        param2=8,
        minRadius=10,
        maxRadius=50)
    # print(circles[0][0])
    print(len(circles[0]))
    if circles is not None:
        for i in range(len(circles[0])):
            x, y, radius = circles[0][i]
            # print(x,y,radius)
            center = (x, y)
            cv2.circle(img, center, radius, (0, 255, 255), 2)
    return img


if __name__ == "__main__":
    img = cv2.imread('redpoint1.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = readimage(img)
    cv2.imwrite('r.png', img)

    #cap = cv2.VideoCapture(0)
    #cv2.namedWindow('result', 0)
    #success, frame = cap.read()
    #while(success):
        #frame = readimage(frame)
        #cv2.imshow('result', frame)
        #key = cv2.waitKey(10)
        #if key == 27:
            #break
        #success, frame = cap.read()
