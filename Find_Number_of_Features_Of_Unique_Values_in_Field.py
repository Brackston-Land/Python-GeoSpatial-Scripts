#-------------------------------------------------------------------------------
# Author:      Brackston Land
# Created:     04/20/2020
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
