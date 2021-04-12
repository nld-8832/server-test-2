import requests

url = "http://3.0.61.179:5000/upload/khoi"
#url = "http://127.0.0.1:5000/upload/khoi"
files = {'files': open('TEST_FILE_2/khoi.wav', 'rb')}
r = requests.post(url, files=files)