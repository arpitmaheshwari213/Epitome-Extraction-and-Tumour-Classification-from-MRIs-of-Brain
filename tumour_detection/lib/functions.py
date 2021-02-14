#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 04:26:41 2018

@author: arpit
"""
import os # for doing directory operations 
import pandas as pd
import nibabel as nib
import numpy as np
import cv2
import math


#path of folders
#file_path='/home/arpit/Desktop/Project'
file_path = os.getcwd()

#folder name
data_dir = file_path+'/Smooth/'
#listing of all folder in data_dir
patients = os.listdir(data_dir)
#used in reshape to decrease fix size of slices eg:60->20 by chunk_size of 3
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
#used to merge slices by taking mean of them  
def mean(l):
    return sum(l) / len(l)

def preprocess_data(patient,labels_df,img_px_size=50, hm_slices=20, visualize=False):
    #patient of type smooth_LGG-343_T2.nii.gz
    path = data_dir + patient
    #print(path)
    
    #convert smooth_LGG-343_T2.nii.gz to LGG-343
    s_patient=str(patient)
    split_patient=s_patient.split('_')
    #read label of LGG-343
    label = labels_df.get_value(split_patient[1], 'Grade')
    
    #load nifti file as numpy array
    img = nib.load(path) 
    img_data =img.get_data()
    shape=img_data.shape
    
    #resize slices from 256*256 to 64*64
    slices = [cv2.resize(img_data[:,:,i],(img_px_size,img_px_size)) for i in range(0,shape[2])]
    
    #make slice no. = 20
    new_slices = []
    chunk_sizes = math.ceil(len(slices) / hm_slices)
    for slice_chunk in chunks(slices, chunk_sizes):
        slice_chunk = list(map(mean, zip(*slice_chunk)))
        new_slices.append(slice_chunk)
    #print(len(slices),len(new_slices))
    empty_slice=list(np.zeros([img_px_size,img_px_size]))
    
    for i in range(0,hm_slices-len(new_slices)):
        new_slices.append(empty_slice)
        
    print(len(slices),len(new_slices))
      
    return new_slices,label