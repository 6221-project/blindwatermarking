#!/usr/bin/env python
# -*- coding: utf8 -*-

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


# load image
def load_image(path):
    img = cv2.imread(path)
    return img


# save image
def save_image(img, path):
    cv2.imwrite(path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


# complement of original img
def complement(img):
    ic = 255 - img
    return ic


# 3D to 1D
def three2one(img):
    one = img.flatten()
    return one


# im2double
def im2double(img):
    info = np.iinfo(img.dtype)
    return img.astype(np.float) / info.max


# transform bgr to rgb
def bgr_to_rgb(img):
    b, g, r = cv2.split(img)
    return cv2.merge([r, g, b])


# get real part of image
def real(img):
    return np.real(img)


# show image
def show_image(img):
    # plt.subplot(111), plt.imshow(bgr_to_rgb(img)), \
    # plt.title('img')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# Fourier transform
def fft(img):
    f = np.fft.fft2(img)
    return f


# inverse Fourier transform
def ifft(img):
    iff = np.fft.ifft2(img)
    return iff


# shift image
def shift(img):
    s = np.fft.fftshift(img)
    return s


# shuffle image
def shuffle_image(img, seed=8888):
    img2 = np.zeros(img.shape)
    random.seed(seed)
    m = list(range(img.shape[0]))
    n = list(range(img.shape[1]))
    random.shuffle(m)
    random.shuffle(n)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img2[i][j] = img[m[i]][n[j]]
    return img2


# shuffle image with reshape
def shuffle_image_with_shape(img, shape, seed=8888):
    img2 = np.zeros(shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img2[i][j] = img[i][j]
    return shuffle_image(img2, seed)


# reverse shuffle
def reverse_shuffle(img, seed=8888):
    random.seed(seed)
    m = list(range(img.shape[0]))
    n = list(range(img.shape[1]))
    random.shuffle(m)
    random.shuffle(n)
    img2 = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # img2[m[i]][n[j]] = np.uint8(img[i][j])
            img2[m[i]][n[j]] = img[i][j]
    return img2

def optimal_shape(img):
    rows = img.shape[0]
    cols = img.shape[1]
    nrows = cv2.getOptimalDFTSize(rows)
    ncols = cv2.getOptimalDFTSize(cols)
    nimg = np.zeros((nrows,ncols,img.shape[2]))
    nimg[:rows,:cols] = img
    return nimg
