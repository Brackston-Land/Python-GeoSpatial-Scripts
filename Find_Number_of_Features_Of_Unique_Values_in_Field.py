'''
The purpose of this script is to identify the number
of features of unique values in arcpy fields.

Authors:       Brackston Land, Blake Herrera
Created:       04/20/2020
'''

# Standard libraries
from collections import Counter
from operator import itemgetter
from pprint import pprint

# Other libraries
import arcpy


fc = r"path to database connections"
field = "wmConsumerType"

with arcpy.da.SearchCursor(fc, field) as cursor:
    # Count all of the first item in each row and format the print string
    pprint(Counter(map(itemgetter(0), cursor)), width = 1)
