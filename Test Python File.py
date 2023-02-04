import request

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)

open('p3 log file', 'wb').write(r.content)
