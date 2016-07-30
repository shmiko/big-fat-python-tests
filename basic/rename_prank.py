import os
from os import listdir
# import glob

# print glob.glob("~/Downloads/prank")
vDir = "~/Downloads/prank"
# os.listdir("~/Downloads/prank")
# filenames = next(os.walk("~/Downloads/prank"))[2]


def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(vDir)

for f in full_file_paths:

  if f.endswith(".dat"):

    print f


def rename_files():
	#get a list of files from a directory

	#for each file rename

