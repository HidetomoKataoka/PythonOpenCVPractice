# coding: utf-8

import numpy as np
import cv2


# 画像をnp.arrayとして読み込む
img = cv2.imread('lenaColCd.png')

# 画像の各チャンネルを取得
img_rgb = cv2.split(img);
imgR = img_rgb[2]
imgG = img_rgb[1]
imgB = img_rgb[0]

#RGB各画像を表示する 
cv2.imshow('original', img )
cv2.imshow('R', imgR)
cv2.imshow('G', imgG)
cv2.imshow('B', imgB)

# wait key input
cv2.waitKey(0)