"""cvlib.py
This file hosts multiple functions that will be used frecuently on the CV course.

Author: Juan Carlos Chávez Villarreal
Contact: juan.chavezv@udem.edu
Organisation: Universidad de Monterrey
First created on Monday 11 March 2024
"""
import cv2
import numpy as np
import sys
import argparse

def read_image(filename):
    img = cv2.imread(filename)
    if img is None:
        print(f"ERROR! - Image {filename} could not be read!")
        return -1
    rows, cols, _ = img.shape
    return img, rows, cols

def rotate_image(img,angle):
    """
    rotates an image the amount of degrees specified

    Parameters:
        img: "Tupla" of the image (image matrix, rows, cols)

        angle: degrees to be rotated
    """
    M = cv2.getRotationMatrix2D((img[2]/2, img[1]/2), angle, 1) #45° degrees
    img_rotated = cv2.warpAffine(img[0], M, (img[2], img[1]))
    return img_rotated

def translate_image(img,tx,ty):
    """
    rotates an image the amount of degrees specified

    Parameters:
        img: "Tupla" of the image (image matrix, rows, cols)

        tx: horizontal translation

        ty: vertical translation
    """
    M = np.float32([[1, 0, tx], [0, 1, ty]]) #50 pxls to the right and 50 pxls down
    img_translated = cv2.warpAffine(img[0], M, (img[2], img[1]))
    return img_translated

def flip_image(img,fp):
    """
    rotates an image the amount of degrees specified

    Parameters:
        img: image

        fp: 0: Flips the image horizontally (along the X-axis)
            1: Flips the image vertically (along the Y-axis)
            -1 (or any negative value): Flips the image along both axes (diagonally)

    """
    img_reflected = cv2.flip(img, fp) # Horizontal flipping
    return img_reflected

def resize_image(img):
    """
    resize image to 1/4
    """
    width = int(img.shape[1] * 0.47)
    height = int(img.shape[0] * 0.47)
    dim = (width, height)
    resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized_img

def visualize_image(img,title):
    resized = resize_image(img)
    cv2.imshow(title, resized)
    cv2.waitKey(0)

def close_windows():
    cv2.destroyAllWindows()