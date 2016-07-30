import os
from os import listdir
# import glob

# print glob.glob("~/Downloads/prank")
vDir = "/Users/pauljones/Downloads/prank"
# os.listdir(vDir)
# filenames = next(os.walk(vDir))[2]
# print (filenames)

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    # print("test paths and filenames now")
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

            # print file_paths
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(vDir)

# for f in full_file_paths:

  # if f.endswith(".dat"):

    # print f


def rename_files(thisDir):
	#get a list of files from a directory
	# vDir = "/Users/pauljones/Downloads/prank"
	# os.listdir(thisDir)
	# filenames = next(os.walk(thisDir))[2]
	# print (filenames)
	file_list = os.listdir(thisDir)
	# filenames = next(os.walk(file_list))[2]
	# print(file_list)
	saved_path = os.getcwd()
	print("Current Directory is "+saved_path)
	os.chdir(r"/Users/pauljones/Downloads/prank")
	#for each file rename
	# os.rename(src, dst),os.renames(old, new)
	#add exception handling if no file is found
	for file_name in file_list:
		print("original file name is " + file_name)
		print("new filename is " + file_name.translate(None,"0123456789"))
		os.renames(file_name,file_name.translate(None,"0123456789"))
	os.chdir(saved_path)	
rename_files(vDir)
