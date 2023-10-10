# Import os module
import os

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"

# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
    search_path = "."


def listdirs(rootdir):
    for file in os.listdir(rootdir):
        current_directory = os.path.join(rootdir, file)
        if os.path.isdir(current_directory):

            # Repeat for each file in the directory
            for fname in os.listdir(current_directory):

                # Apply file type filter
                if fname.endswith(file_type):
                    try:
                        # print(fname)
                        current_file = os.path.join(current_directory, fname)
                        # Open file for reading
                        fo = open(current_file)

                        # Read the first line from the file.py
                        line = fo.readline()

                        # Initialize counter for line number
                        line_no = 1

                        # Loop until EOF
                        while line != '':

                            # Search for string in line
                            index = line.find(search_str)
                            if (index != -1):
                                print(fname, "[", line_no, ",",
                                      index, "] ", line, sep="")

                            # Read next line
                            line = fo.readline()

                            # Increment line counter
                            line_no += 1
                        # Close the files
                        fo.close()

                    except:
                        print("An exception occurred")

                        # use recursion to check next folder
                        # listdirs(current_directory)


rootdir = search_path
listdirs(rootdir)
