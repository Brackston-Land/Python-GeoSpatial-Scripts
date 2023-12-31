#-------------------------------------------------------------------------------
# Author:      Brackston Land
# Created:     04/22/2020
#-------------------------------------------------------------------------------

#https://community.esri.com/thread/121876
import arcpy

sdeconnection = r"your connection here"

edit = arcpy.da.Editor(sdeconnection)
print "edit created"
try:
    edit.startEditing()
    print "edit started"
    edit.startOperation()
    print "operation started"
    # Perform edits
    with arcpy.da.InsertCursor(fc, fields) as fc_icursor:
        fc_icursor.insertRow(someNewRow)
    edit.stopOperation()
    print "operation stopped"
    edit.stopEditing(True)  ## Stop the edit session with True to save the changes
    print "edit stopped"
except Exception as err:
    print err
    if edit.isEditing:
        edit.stopOperation()
        print "operation stopped in except"
        edit.stopEditing(False)  ## Stop the edit session with False to abandon the changes
        print "edit stopped in except"
finally:
    # Cleanup
    arcpy.ClearWorkspaceCache_management()
