#Import os module
import os

# Ask the user to enter string to search
#search_path = input("Enter directory path to search : ")
#file_type = input("File Type : ")
#search_str = input("Enter the search string : ")

# if nothing is entered by user then use these default values
search_path = 'H:\Prism Report Exports\myCVS\ISAust Prism Reports\SO'
file_type = 'txt'
search_str = 'SH_PRIORITY'

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"

# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):

   # Initialize counter for file number
   file_no = 1

   # Apply file type filter   
   if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :
                    print("No: ",file_no, " ", fname, "[", line_no, "", index, "] ", line, sep=",")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()
