#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brackston Land
#
# Created:     13/01/2020
# Copyright:   (c) Brackston Land 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

import json

# For each field in the Hospitals feature class, print
#  the field name, type, and length.
fields = arcpy.ListFields("Database Connections\YourSDE.sde\FeatureClass")

for field in fields:
    print(field.name, field.type)

    #print (json.dumps(field.name) + ", ")

