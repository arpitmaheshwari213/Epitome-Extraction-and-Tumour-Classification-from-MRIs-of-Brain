#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:50:51 2018

@author: arpit
"""

import nibabel as nib
import matplotlib.pyplot as plt
import os,math
import numpy as np
import matplotlib.gridspec as gridspec


'''def show_slices(slices,x):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(x/4,4)       # changes as per the length of slice
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
'''


def save_image_as_jpeg(input_file):
    #input_file = os.getcwd()+input_img
    img = nib.load(input_file)
    img_data = img.get_data()
    shape = img_data.shape 
    slice_list=[]
    for i in range(0,shape[2]):               #for different parts scanned during MRI 
        slice_list.append(img_data[:, :, i])         # making a 3D matrix

    
    plt.suptitle("Original NIfTI Images")
    fig=plt.figure(figsize=(5,10))
    plt.axis('off')
    columns = 5
    rows = math.ceil((shape[2])/5)
    gs1 = gridspec.GridSpec(rows,columns)
    gs1.update(wspace=0.05, hspace=0.05)
    for i in range(0,shape[2]):
    #img = np.random.randint(10, size=(h,w))
        fig.add_subplot(gs1[i],xticks=[],yticks=[])
        plt.imshow(slice_list[i],cmap="gray",origin="upper",aspect="auto")
    fig.subplots_adjust(wspace=0,hspace=0)
    plt.savefig(input_file+'.jpg',bbox_inches='tight')
    #plt.show()


