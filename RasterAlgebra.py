import arcpy 
from arcpy.sa import * 

# Specify the input raster 
inRaster = r"C:\PSU\Geog489\Lesson1\Rasters\foxlake" 
cutoffElevation = 3500

# Check out the Spatial Analyst extension 
arcpy.CheckOutExtension("Spatial") 

# Make a map algebra expression and save the resulting raster 
outRaster = Raster(inRaster) > cutoffElevation 
outRaster.save(r"C:\PSU\Geog489\Lesson1\Rasters\foxlake_hi_10") 

# Check in the Spatial Analyst extension now that you're done 
arcpy.CheckInExtension("Spatial") 