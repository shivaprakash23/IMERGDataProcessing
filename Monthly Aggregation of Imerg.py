import arcpy,os
from arcpy.sa import *
#TestFolder="E:\\shiva\\LOCUST\\Precipitation\\Imerg\\OutResult\\05"
TestFolder=arcpy.GetParameterAsText(0)
arcpy.env.workspace=TestFolder
#Result = "E:\\shiva\\LOCUST\\Precipitation\\Imerg\\MonthlyAggregation"
Result=arcpy.GetParameterAsText(1)
rasterlist= arcpy.ListRasters("*","TIF")

AggregateRaster=0.0

for raster in rasterlist:
	AggregateRaster=AggregateRaster+Raster(raster)

AggregateRaster.save(Result+"\\"+rasterlist[0])

