#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brackston Land
#
# Created:     20/04/2020
# Copyright:   (c) Brackston Land 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

fc = r"path to database connections"
field = "wmConsumerType"

#Create dictionary to store unique values
CountDi = {}

with arcpy.da.SearchCursor (fc, field) as cursor:
    for row in cursor:
        if not row[0] in CountDi.keys():
            CountDi[row[0]] = 1
        else:
            CountDi[row[0]] += 1

for key in CountDi.keys():
    print str(key) + ":", CountDi[key], "features"