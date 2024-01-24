# Author: Brackston Land
# Created: 1/24/2024     

# ================================================
# WARNING: BACK UP YOUR DATA BEFORE USING THIS SCRIPT
# ================================================
# This script is designed to compress a database. 
# Use it at your own risk. Make sure to create a backup 
# of your data before running this script to avoid any 
# potential loss of information.

#For more information about compressing geodatabases see: 
#https://desktop.arcgis.com/en/arcmap/latest/manage-data/gdbs-in-sql-server/geodatabase-compress-operation.htm


import arcpy
import logging
import os

# Set the path to the script location
script_path = os.path.dirname(os.path.abspath(__file__))

# Set up logging configuration
log_path = os.path.join(script_path, 'logfile.log')
logging.basicConfig(filename=log_path, level=logging.INFO)


# Declare module-level variables:
yourSDE = "C:\\Users\\user\\AppData\\Roaming\\ESRI\\Desktop10.x\\ArcCatalog\\YourSDE.sde"


#Disconnect all users
try:
   
    #Get a list of connected users
    userList = arcpy.ListUsers(yourSDE)

    #Pull userNames from userList
    userNames = [uL.Name for uL in userList]
    logging.info("These users are connected: " + str(userNames))

    #Disable connections
    arcpy.AcceptConnections(yourSDE, False)
    logging.info("the database is no longer accepting connections")

    #Disconnect all users from the database
    arcpy.DisconnectUser(yourSDE, "ALL")
    logging.info("Disconnecting " + str(userNames))

except arcpy.ExecuteError as e:
    logging.error(f"There is an error with disconnecting users from databases: {e}")


#adds a blank line in the logger for readability
logging.info("\n")


try:

    # Compress: Compresses an enterprise geodatabase by removing states 
    # not referenced by a version and redundant rows.
    arcpy.Compress_management(yourSDE)
    logging.info("arcpy.Compress_management complete \n")

    # Rebuild Indexes: Rebuilds existing attribute or spatial indexes in 
    # enterprise geodatabases.
    arcpy.RebuildIndexes_management(yourSDE, "SYSTEM", "", "ALL")
    logging.info("Indexes rebuilt \n")

    # Analyze Datasets: Updates database statistics of base tables, delta tables, 
    # and archive tables, along with the statistics on those tables' indexes. 
    arcpy.AnalyzeDatasets_management(yourSDE, "SYSTEM", "", "ANALYZE_BASE", "ANALYZE_DELTA", "ANALYZE_ARCHIVE")
    logging.info("Datasets have been analyzed \n")


except arcpy.ExecuteError as e:
    logging.error(f"There is an error with the arcpy compression: {e}")


try:
    #Allow connections to the database
    arcpy.AcceptConnections(yourSDE, True)
    logging.info("the database now accepting connections again")

except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")

logging.info("End of Script")