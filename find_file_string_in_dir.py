import glob,os

data_dir = 'H:\Prism Report Exports\myCVS'
file_dir_extension = os.path.join(data_dir, '*.txt')

for file_name in glob.glob(file_dir_extension):
    if file_name.endswith('.txt'):
        print (file_name)
		with open(file_name) as f:   # open file
			for line in f:       # process line by line
				if 'kmart' in line:    # search for string
					print ('ok ' line)
					break