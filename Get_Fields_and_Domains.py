#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brackston Land
#
# Created:     30/09/2021
# Copyright:   (c) Brackston Land 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
#Set workspace environment to geodatabase
arcpy.env.workspace = r"Database Connections\YourSDE.sde\FeatureClass"

#Get list of feature classes in geodatabase
FCs = arcpy.ListFeatureClasses()

#Loop through feature classes in list
for FC in FCs:

        #List fields in feature class
        fields = arcpy.ListFields(FC)

        #Loop through fields
        for field in fields:

            #Check if field has domain
            if field.domain != "":

                #Print feature class, field, domain name
                print(FC, ",", field.name, ",", field.domain)
##            else:
##                  print FC, ",", field.name

#Get list of tables in geodatabase
TBs = arcpy.ListTables()

#Loop through tables in list
for TB in TBs:

        #List tables in feature dataset
        fields = arcpy.ListFields(TB)

        #Loop through fields
        for field in fields:

            #Check if field has domain
            if field.domain != "":

                #Print table, field, domain name
                print(TB, ",", field.name, ",", field.domain)
