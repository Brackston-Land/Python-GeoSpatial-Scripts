import arcpy
import pandas as pd

def load_df (fc, fields, sr=None): 
    datalist=[]
    
    #put all fields from the feature class into a list for the search cursor.
    if fields==['*']: 
        fields=[f.name for f in arcpy.ListFields (fc)]+[ 'SHAPE@']
        
    with arcpy.da.SearchCursor(fc, fields,spatial_reference=sr) as cursor:
        for row in cursor: 
            data={} 
            for i in range(0, len(fields)): 
                data[fields[i]]=row[i] 
            datalist.append(data)
            
    
    return pd.DataFrame(datalist)