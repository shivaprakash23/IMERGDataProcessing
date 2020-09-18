import arcpy,os
from arcpy.sa import *
#TestFolder="E:\\shiva\\LOCUST\\Precipitation\\Imerg\\Data"
TestFolder=arcpy.GetParameterAsText(0)
arcpy.env.workspace=TestFolder
#Result = "E:\\shiva\\LOCUST\\Precipitation\\Imerg\\OutResult"
Result=arcpy.GetParameterAsText(1)
rasterlist=os.listdir(TestFolder)
projection = arcpy.SpatialReference(4326)

	
#3B-DAY-L.MS.MRG.3IMERG.20200501-S000000-E235959.V06.nc4
for raster in rasterlist:
	name=raster.split('.')
	name1=name[3]
	name2=name[4].split('-')[0]
	newName="n"+str(name1)+"_"+str(name2)
	newSubFolder=str(name2[4:6])
	filename=Result+"\\"+newSubFolder+"\\"+newName+".tif"
	path=Result+"\\"+newSubFolder

        # Set local variables
        inNetCDFFile = TestFolder+"\\"+raster
        variable = "precipitationCal"
        XDimension = "lon"
        YDimension = "lat"
        outRasterLayer = newName
        bandDimmension = ""
        dimensionValues = ""
        valueSelectionMethod = "BY_VALUE"
		
	if os.path.exists(path):
		print("Folder exists"+newSubFolder)
		arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable, XDimension, YDimension,outRasterLayer, bandDimmension, dimensionValues,valueSelectionMethod)
		arcpy.CopyRaster_management(outRasterLayer,filename,"","","","","","","","","TIFF","")
                #Outfilename.save(filename)
		#arcpy.Delete_management(outRasterLayer)
	else:
		arcpy.CreateFolder_management(Result,newSubFolder)
		print("Folder exists"+newSubFolder)
		arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable, XDimension, YDimension,outRasterLayer, bandDimmension, dimensionValues,valueSelectionMethod)
		arcpy.CopyRaster_management(outRasterLayer,filename,"","","","","","","","","TIFF","")
                #Outfilename.save(filename)
		#arcpy.Delete_management(outRasterLayer)

