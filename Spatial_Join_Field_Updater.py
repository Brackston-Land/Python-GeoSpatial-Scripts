'''
This script updates specified fields in a feature class based on spatial join 
results with one or more additional feature classes. 
The spatial join outputs to a temporary feature class in memory which is deleted after the 
desired information is pulled from it.

Authors: Brackston Land
Created: 2024
'''

import arcpy
import os

yourdatabase = r"C:\....\MyProject\MyProject.gdb"

arcpy.env.workspace = yourdatabase

arcpy.env.overwriteOutput = True

target_fc = os.path.join(yourdatabase, "your_featureclass_name")
joining_fc_1 = r"https://......./FeatureServer/0"  # example feature service
# example feature class
joining_fc_2 = r"C:\....\MyProject\MyProject.gdb\joining_feature_class"


def spatial_join_field_updater(target, joining, target_fields, joining_fields):

    try:
        # Check if target_fields and joining_fields have the same length
        if len(target_fields) != len(joining_fields):
            raise Exception(
                "Error: target_fields and joining_fields must have the same length.")

        # Output feature class (temporary)
        temp_spatial_join_fc = arcpy.CreateUniqueName(
            "temp_spatial_join", "in_memory")

        arcpy.analysis.SpatialJoin(
            target_features=target,
            join_features=joining,
            out_feature_class=temp_spatial_join_fc,
            join_operation="JOIN_ONE_TO_ONE",
            join_type="KEEP_ALL",
            field_mapping='',
            match_option="HAVE_THEIR_CENTER_IN",
            search_radius=None,
            distance_field_name="")

        # Update specified fields in parcels based on spatial join results
        with arcpy.da.UpdateCursor(target, target_fields) as update_cursor:
            with arcpy.da.SearchCursor(temp_spatial_join_fc, joining_fields) as search_cursor:
                print("working on updates")
                for update_row, search_row in zip(update_cursor, search_cursor):
                    # Update fields dynamically
                    for i in range(len(joining_fields)):
                        update_row[i] = str(search_row[i])
                    update_cursor.updateRow(update_row)

        print("finished with updates")

    except Exception as e:
        print("Exception:", e)
    finally:
        # Clean up the temporary feature class
        if arcpy.Exists(temp_spatial_join_fc):
            arcpy.Delete_management(temp_spatial_join_fc)
            print("deleted temporary feature class")


'''
note: if you have matching names in the two feature classes you are going to spatial join, 
one of them will have something appended (usually _1) to the end. So if you are updating NAME in target with NAME in joining, 
the name in joining after the spatial join will likely be NAME_1
target_fields_list = ["NAME"]
joining_fields_list = ["NAME_1"]
'''

# run for first dataset
target_fields_list = ["stateCode", "temp"]
joining_fields_list = ["STATE", "Temperature"]
spatial_join_field_updater(target_fc, joining_fc_2,
                           target_fields_list, joining_fields_list)

# run again for second data set
target_fields_list = ["team"]
joining_fields_list = ["team_name"]
spatial_join_field_updater(target_fc, joining_fc_1,
                           target_fields_list, joining_fields_list)
