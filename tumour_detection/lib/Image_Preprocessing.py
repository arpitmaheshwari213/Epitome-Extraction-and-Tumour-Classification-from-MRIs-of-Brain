#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:28:41 2018

@author: arpit
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:18:29 2018

@author: Chayan-Dhaddha
"""

import os # for doing directory operations 
#import pandas as pd

import numpy as np
from nipype.interfaces import fsl
#import matplotlib.pyplot as plt

file_path='/home/arpit/Desktop/Project'
data_dir = file_path+'/NiFTiSegmentationsEdited/'
patients = os.listdir(data_dir)
#len(patients)


for patient in patients[:]:
    #print(patient)
    path = data_dir + patient
    input_file = path + '/' + patient+'_T2.nii.gz'
    print(input_file)
    #Preprocessing 
    #Skull Stripping  /home/arpit/Desktop/Project/Skull _Stripped
    output_strip_file = "skull_stripping_"+patient+"_T2.nii.gz"
    skullstrip = fsl.BET(in_file=input_file, out_file=file_path+'/Skull_Stripped/'+output_strip_file,mask=True)
    skullstrip.run()

    #Inhomogeneity Correction(Smoothing)
    output_smooth_file = "smooth_"+patient+"_T2.nii.gz"
    smooth = fsl.IsotropicSmooth(in_file=file_path+'/Skull_Stripped/'+output_strip_file, out_file=file_path+'/Smooth/'+output_smooth_file,fwhm=4)
    smooth.run()