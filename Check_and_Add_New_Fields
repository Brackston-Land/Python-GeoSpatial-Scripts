'''
This script checks if specified fields already exist. 
If they do not exist the fields are created.

Authors: Brackston Land
Created: 2024
'''

import arcpy
import os

yourdatabase = r"C:\....\MyProject\MyProject.gdb"

arcpy.env.workspace = yourdatabase
arcpy.env.overwriteOutput = True

target_fc = os.path.join(yourdatabase, "target_fc")

def check_and_add_new_fields(target_fc, new_field_names):

    # Get a list of existing fields
    existing_fields = [field.name for field in arcpy.ListFields(target_fc)]

    # Add new fields
    for field in new_field_names:
        # Check if the field already exists
        if field in existing_fields:
            print(
                f"The field '{field}' already exists in the feature class or table.")
        else:
            # If the field doesn't exist, add it
            arcpy.management.AddField(
                in_table=target_fc,
                field_name=field,
                field_type=new_field_names[field],
                field_precision=None,
                field_scale=None,
                field_length=None,
                field_alias="",
                field_is_nullable="NULLABLE",
                field_is_required="NON_REQUIRED",
                field_domain=""
            )
            print(
                f"The field '{field}' has been added to the feature class or table.")


# Name and tpyes of the fields to add
new_field_names = {"test_name": "TEXT", "score": "LONG"}
check_and_add_new_fields(target_fc, new_field_names)
