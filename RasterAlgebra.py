# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:21:15 2023

@author: habib
"""

# This script uses map algebra to find values in an 
#  elevation raster greater than 3500 (meters). 

import arcpy 
from arcpy.sa import * 

# Specify the input raster 
inRaster = r"C:\PSU\Geog489\Lesson1\Rasters\foxlake" 
cutoffElevation = 2000

# Check out the Spatial Analyst extension 
arcpy.CheckOutExtension("Spatial") 

# Make a map algebra expression and save the resulting raster 
outRaster = Raster(inRaster) > cutoffElevation 
outRaster.save(r"C:\PSU\Geog489\Lesson1\Rasters\foxlake_hi_10") 

# Check in the Spatial Analyst extension now that you're done 
arcpy.CheckInExtension("Spatial") 