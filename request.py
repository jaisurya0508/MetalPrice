import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'commodity':0, 'S3':1788, 'S9':1888, 'Year':2021, 'Month(in number)':5,'Date':7 })

print(r.json())


