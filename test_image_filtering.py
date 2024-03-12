"""test_image_filtering
This code applies the following filters to an image:
    - median
    - average
    - Gaussian

Author: Juan Carlos Chávez Villarreal
Contact: juan.chavezv@udem.edu
Organisation: Universidad de Monterrey
First created on Monday 11 March 2024
"""
import cv2
import numpy as np
import sys
import argparse
import cvlib as cvl

def parse_user_data():
    parser = argparse.ArgumentParser(prog='HW5 - Image Filter Aplication', 
                                    description='Apply filter transformations to a user inputed image using OpenCV library.', 
                                    epilog='JCCV - 2024')
    parser.add_argument('-img',
                        '--input_image',
                        type=str,
                        required=True,
                        help="Path to the input image")
    
    parser.add_argument('-flt',
                        '--input_filter',
                        type=str,
                        required=True,
                        help="Filter to be applied to the input image (median,average, or Gaussian)")
    
    parser.add_argument('-fk',
                        '--filter_kernel',
                        type=int,
                        required=True,
                        help="Kernel for the Filter")
    
    args = parser.parse_args()
    return args

def median_filter(img,fk):
    img_median = cv2.medianBlur(img,fk)
    return img_median

def average_filter(img,fk):
    img_average = cv2.blur(img,(fk,fk))
    return img_average

def gaussian_filter(img,fk):
    img_gaussian = cv2.GaussianBlur(img,(fk,fk),0)
    return img_gaussian

def pipeline():
    args = parse_user_data()

    # Load the image
    img = cvl.read_image(args.input_image)
    
    fil = args.input_filter
    fk = args.filter_kernel

    if fil == "median":
        out_img = median_filter(img,fk)
    elif fil == "average":
        out_img = average_filter(img,fk)
    elif fil == "gaussian":
        out_img = gaussian_filter(img,fk)  # Corrected to pass img instead of 0

    # Display the original and filtered images
    cvl.visualize_image(img, 'Input Image')
    cvl.visualize_image(out_img, fil)


if __name__ == '__main__':
    pipeline()