import re
import datetime
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

with open(r"/home/nguyendy/project3logfile.txt", 'r') as fp: #this line is where you'd need to change your file path
    x = len(fp.readlines())
    start_date = datetime.datetime(1995, 4, 11)
    y = 0
    for line in fp:
        log_date = datetime.datetime.strptime(line.split()[3][1:], '%d/%b/%Y:%H:%M:%S')
        if log_date >= start_date:
            y += 1

print("Number of total requests in the 6 months:", y)
print('The total amount of requests in the log file is: ', x)

