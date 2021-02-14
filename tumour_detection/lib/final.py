# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:18:29 2018

@author: Chayan-Dhaddha
"""

import os # for doing directory operations 
import pandas as pd

import numpy as np

from functions import *
#from nipype.interfaces import fsl
#import matplotlib.pyplot as plt

#used to reshape and resize
IMG_PX_SIZE = 64
NUM_SLICES = 20



#path of folders
#file_path='/home/arpit/Desktop/Project'
file_path = os.getcwd()

#folder name
data_dir = file_path+'/Smooth/'
#listing of all folder in data_dir
patients = os.listdir(data_dir)

#resize & reshape all nifti file to  64*64*20

   
    
#get labels from xlsx file
labels_df=pd.ExcelFile(file_path+"/TCIA_LGG_cases_159.xlsx")
labels_df=labels_df.parse("Sheet1",index_col=0)
labels_df=labels_df.drop(['1p/19q','Type'],axis=1)
#print(labels_df)        

final_img=[]
final_labels=[]
for patient in patients[:]:
    print("hiii ",patient)
    
    img_data,label=preprocess_data(patient,labels_df,img_px_size=IMG_PX_SIZE, hm_slices=NUM_SLICES)
    #print(img_data,label)
    """if label==2:
        file_out = file_path + "/final_data/benign/"
    elif label==3:
        file_out = file_path + "/final_data/malignant/" """
    final_img.append([img_data])
    
    final_labels.append(label-2)
    print(np.array(img_data).shape)
    #convert smooth_LGG-343_T2.nii.gz to LGG-343
    #s_patient=str(patient)
    #split_patient=s_patient.split('_')
    #np.save(file_out+'final_img-{}-{}-{}-{}.npy'.format(split_patient[1],IMG_PX_SIZE,IMG_PX_SIZE,NUM_SLICES),final_img)
np.save(file_path+'/final_img-{}-{}-{}.npy'.format(IMG_PX_SIZE,IMG_PX_SIZE,NUM_SLICES),final_img)
np.save(file_path+'/final_labels.npy',final_labels)   
print(np.array(final_img).shape)
    