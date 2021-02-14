# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:18:28 2018

@author: Chayan-Dhaddha
"""
#from cnn import *
#from lib.functions import chunks,mean
import nibabel as nib
import cv2
import math
import numpy as np
import os


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


# used to merge slices by taking mean of them
def mean(l):
    return sum(l) / len(l)

def preprocess_test_data(patient,img_px_size=64, hm_slices=20, visualize=False):
    #patient of type smooth_LGG-343_T2.nii.gz
    
    #print(type(patient))
    
    #print(path)
     
    #load nifti file as numpy array
    img = nib.load(patient) 
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
        
    return new_slices
   
def output(x):
    
    """ file_path = os.getcwd()
    data_dir = file_path+'/Test/'
    test_patient = os.listdir(data_dir)"""
    
    img_data = preprocess_test_data(x)
    test_data=[]
    test_data.append(img_data)

    #np.save(file_path+'/test_img.npy',test_data)
    #print(test_data)
    test_data=np.array(test_data).transpose(3,2,1,0)
    data=[]
    data.append([test_data])
    from keras import backend as K                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    K.clear_session()
    from keras.models import load_model
    classifier = load_model(os.getcwd()+'/lib/brain_model.h5')
    y_pred = classifier.predict(np.array(data[0]))
    y_pred = (y_pred > 0.5)

    #print(y_pred)
    if (y_pred==False):
        return 0
    else:
        return 1


"""file_path = os.getcwd()
data_dir = file_path+'/Test/smooth_LGG-104_T2.nii.gz'

print(output(data_dir))
 """

