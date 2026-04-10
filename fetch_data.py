import requests
import json

# API link is svaed in url variable
url= "https://hn.algolia.com/api/v1/search?tags=front_page" 

#send request and check
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
  print("Error")
  exit()

# Save as JSON file
with open("raw_data.json", "w") as f:
  json.dump(data, f)
print("JSON file saved")
