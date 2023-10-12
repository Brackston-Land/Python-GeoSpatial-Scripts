'''
Authors:        Brackston Land, Blake Herrera
Created:        09/30/2021
'''

from operator import attrgetter

import arcpy
#Set workspace environment to geodatabase
arcpy.env.workspace = r"Database Connections\YourSDE.sde\FeatureClass"


def get_fields(containers):
    ''' Prints out all field names with a domain.'''
    for container in containers:
        # Only iterate through fields with a domain
        for field in filter(attrgetter('domain'), arcpy.ListFields(container)):
            print(f'{container}, {field.name}, {field.domain}')


#Get list of feature classes and tables in geodatabase
get_fields(arcpy.ListFeatureClasses())
get_fields(arcpy.ListTables())
