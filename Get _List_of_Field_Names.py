#-------------------------------------------------------------------------------
# Author:      Brackston Land
# Created:     01/13/2020
#-------------------------------------------------------------------------------

import arcpy
import json

# For each field in the Hospitals feature class, print
#  the field name, type, and length.
fields = arcpy.ListFields("Database Connections\YourSDE.sde\FeatureClass")

for field in fields:
    print(field.name, field.type)

    #print (json.dumps(field.name) + ", ")
