###############################################
## code pulled from https://community.esri.com/t5/arcgis-survey123-questions/backup-survey-123-feature-layer/td-p/1041504
## Modified by Brackston Land 1/26/2022
## To use: open up the .txt that you create file and 
## on a new line add the output name of the what you want to download, a comma, and the Item ID of the item you want to backup. No spaces.
## Example ----->     Testing222,87858c26de2353255e4cdca32958a58gfg2370667e1

###############################################

import os
import time
from arcgis.gis import GIS


def backup_agol(name: str, id: str, out_dir: str, conn: GIS):
    try:
        print(f"+ [{name}] starting")

        # Get content from AGOL
        fs_link = gis.content.get(id)
        print(f"* get by ID completed with {bool(fs_link)}")
        export = fs_link.export(f"tempOut{name}", "File Geodatabase")
        print(f"* export completed with {bool(export)}")

        # Save to file system
        dt = time.strftime("%Y%m%d_%H%M%S")
        print(f"* using time stamp {dt}")
        out_file = os.path.join(backupDir, f"{name}\{name}_{dt}.zip")
        print(f"* using file name {out_file}")

        export.download(out_dir, out_file)
        print("* completed download")

        # Remove the extracted FGDB from AGOL (cleanup)
        delete_result = export.delete()
        print(f"* deleted extracted data, with {bool(delete_result)}")
    except Exception as e:
        print(e)

 
try:
    #Define Variables
    # Setup inputs
    configFile = r"Path to your .txt file"
    backupDir = r"path to the Downloaded_ZIPS folder"

    # Make a connection to ArcPro

    # If there is an issue with the certificate, use this:
    #gis = GIS('pro',verify_cert=False)
    # Otherwise, this is a public login:
    #gis = GIS('pro')
    # Or, better, use this direct connection:
    gis = GIS("https://arcgis.com", "your user name", "your password")

    with open(configFile) as cfg:
        for hfs in (line.rstrip() for line in cfg):
            backup_agol(*hfs.split(","), backupDir, gis)

except Exception as e:
    print(e)

print("End of Script")

