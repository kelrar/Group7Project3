import re
from os.path import exists 
from urllib.request import urlretrieve 

FILE_NAME = 'project3logfile.txt'

if not exists(FILE_NAME): 
    print("File not found on system. The log file is being retrieved now.")
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'project3logfile.txt'
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    print("The file has been retrieved and saved locally.")
else:
    print("This file is already on your system")

with open(r"C:\Users\black\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11\stuff\project3logfile.txt", 'r') as fp: #this line is where you'd need to change your file path
    x = len(fp.readlines())
    print('Total lines:', x)