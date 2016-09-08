import glob,os

data_dir = 'data_folder/'
file_dir_extension = os.path.join(data_dir, '*.txt')

for file_name in glob.glob(file_dir_extension):
    if file_name.endswith('.txt'):
        print file_name