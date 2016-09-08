import os

for fname in os.listdir('H:\Prism Report Exports\myCVS'):    # change directory as needed
    if os.path.isfile(fname):    # make sure it's a file, not a directory entry
        with open(fname) as f:   # open file
            for line in f:       # process line by line
                if 'kmart' in line:    # search for string
                    print ('found string in file %s ' %fname)
                    break