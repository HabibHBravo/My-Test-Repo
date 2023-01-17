# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:08:49 2023

@author: habib
"""

# Opens a feature class from a geodatabase and prints the spatial reference   
import arcpy 

featureClass = r"C:\PSU\Geog489\Lesson1\Shapes\USA.gdb\States" 

# Describe the feature class and get its spatial reference    
desc = arcpy.Describe(featureClass) 
spatialRef = desc.spatialReference 

# Print the spatial reference name 
print (spatialRef.Name) 