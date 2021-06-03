import requests
import json

url = "https://api.notion.com/v1/pages"

payload = {
    "parent": { "database_id": "f5c1ad2009144d6594702c9f01456b30" },
    "properties": {
      "Name": {
        "title": [
          {
            "text": {
              "content": "Test",
            } } ] } } }
             
        
headers = {'Content-Type': 'application/json' ,
           'Accept': 'application/json' ,
           'Authorization': 'Bearer secret_PPV509kjjN0l47GGFtREOfJ0dNODA7XbPj030IVKkXE' 
                }

r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.status_code)
print(r.content)