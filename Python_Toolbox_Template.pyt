'''
When creating a Python toolbox, the template below is used to form the toolbox. 
This code creates a Python toolbox with a toolbox class named Toolbox, and a single tool named Tool. 
The Tool class should be renamed, and can be duplicated and edited to create additional tools in 
your Python toolbox. The tool name and toolbox alias must begin with a letter (a-z, A-Z) and can 
only consist of letters and numbers (0-9). Spaces and special characters are not allowed 
(for example, _, !, @, #, $, %, -).

Alternatively, the following code could be copied and pasted into a new .pyt file:

https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/a-template-for-python-toolboxes.htm
'''



# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = None
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return