import requests

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)

open('project 3 log file', 'wb').write(r.content)

def count_request(file_path):
    with open(file_path, "r") as log_file:
        lines = log_file.readlines()
        return len(lines)

file_path = "path/to/log/file.log"
total_request = count_request(file_path)
print("Total request:", total_request )



