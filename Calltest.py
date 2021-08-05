import requests
import json

class NotionCall():
    db_nKU_id = ""  #db notKnownUsers ID
    headers = ""
    def __init__(self, apiToken, Db_nKU_id):    #Bearer secret_PPV509kjjN0l47GGFtREOfJ0dNODA7XbPj030IVKkXE
        self.db_nKU_id = Db_nKU_id
        self.headers = {'Content-Type': 'application/json' ,'Accept': 'application/json' ,'Authorization': apiToken}
    def sendNotKnownUsers(self):
        notKnownUsers = {"parent": { "database_id": self.db_nKU_id }, "properties": { "time taken": { "id": "FHfz", "type": "text", "text": [ { "type": "text", "text": { "content": "" }, "annotations": { "color": "default" }, "plain_text": "" } ] }, "time returned": { "id": "GeNQ", "type": "text", "text": [ { "type": "text", "text": { "content": "Test6" }, "annotations": { "color": "default" }, "plain_text": "Test4" } ] }, "date": { "id": "RbPU", "type": "text", "text": [ { "type": "text", "text": { "content": "Test4" }, "annotations": { "color": "default" }, "plain_text": "Test4" } ] }, "key number returned": { "id": "XBSV", "type": "text", "text": [ { "type": "text", "text": { "content": "Test8" }, "annotations": { "color": "default" }, "plain_text": "Test4" } ] }, "Id": { "id": "_GRu", "type": "text", "text": [ { "type": "text", "text": { "content": "Test2" } }]}, "mobile number": { "id": "ydv}", "type": "text", "text": [ { "type": "text", "text": { "content": "Test3" }, "annotations": { "color": "default" }, "plain_text": "Test4" } ] }, "key number picked": { "id": "}?F^", "type": "text", "text": [ { "type": "text", "text": { "content": "Test7" }, "annotations": { "color": "default" }, "plain_text": "Test4" } ] }, "name": { "id": "title", "type": "title", "title": [ { "type": "text", "text": { "content": "Test1" } } ] } }}
        url = "https://api.notion.com/v1/pages"
        status = self.call(content= notKnownUsers, url=url)
        return status
    def call(self, content, url):
        r = requests.post(url, data=json.dumps(content), headers=self.headers)
        return r.status_code

call = NotionCall("Bearer secret_PPV509kjjN0l47GGFtREOfJ0dNODA7XbPj030IVKkXE", "f5c1ad2009144d6594702c9f01456b30")
status = call.sendNotKnownUsers()
print(status)