#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brackston Land
#
# Created:     14/01/2020
# Copyright:   (c) Brackston Land 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##Credit: Josh Werts http://joshwerts.com/blog/2014/04/01/arcpy-rename-fields/


#######for python 3 .iteritems() attribute has been renamed to .items()
import arcpy 
arcpy.env.overwriteOutput = True

def rename_fields(table, out_table, new_name_by_old_name):
    """ Renames specified fields in input feature class/table
    :table:                 input table (fc, table, layer, etc)
    :out_table:             output table (fc, table, layer, etc)
    :new_name_by_old_name:  {'old_field_name':'new_field_name',...}
    ->  out_table
    """
    existing_field_names = [field.name for field in arcpy.ListFields(table)]

    field_mappings = arcpy.FieldMappings()
    field_mappings.addTable(table)

    for old_field_name, new_field_name in new_name_by_old_name.iteritems():
        if old_field_name not in existing_field_names:
            message = "Field: {0} not in {1}".format(old_field_name, table)
            raise Exception(message)

        mapping_index = field_mappings.findFieldMapIndex(old_field_name)
        field_map = field_mappings.fieldMappings[mapping_index]
        output_field = field_map.outputField
        output_field.name = new_field_name
        output_field.aliasName = new_field_name
        field_map.outputField = output_field
        field_mappings.replaceFieldMap(mapping_index, field_map)

    # use merge with single input just to use new field_mappings
    arcpy.Merge_management(table, out_table, field_mappings)
    return out_table


# does need need to include all fields, only those you want to rename
new_name_by_old_name = { 'old_name_1':'new_name_1',
                         'old_name_2':'new_name_2' }
rename_fields(in_fc, renamed_fc, new_name_by_old_name)



