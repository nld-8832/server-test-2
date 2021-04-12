import requests

trans_local_storage = '/Transcribe_File/khoi_save.txt'
url = "3.0.61.179:5000/download/khoi"
#url = "127.0.0.1:5000/download/khoi"
response = requests.get(url)
txt = response.text

with open(trans_local_storage, "a") as text_file:
    text_file.write(txt)
