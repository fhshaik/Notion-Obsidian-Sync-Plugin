from notion2md.exporter.block import MarkdownExporter
import requests
from datetime import datetime, timedelta
import json

import os

jsonpath=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
with open(jsonpath, 'r') as file:
    # Load JSON data as a dictionary
    data = json.load(file)

NOTION_TOKEN=data["NOTION_TOKEN"]
DATABASE_ID=data["DATABASE_ID"]

pastTime=datetime.fromisoformat(data["TIME"])

currentTime=datetime.now().isoformat()
folderpath=data["SYNC_FOLDER"]

data["TIME"]=currentTime
with open(jsonpath, 'w') as json_file:
    json.dump(data,json_file, indent=4)



headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_pages(num_pages=None):
    
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    
    results = data["results"]
    recent=[]
    for a in results:
        if (datetime.fromisoformat(a["last_edited_time"][:-1])>pastTime):
            recent.append(a)

    return recent

pages = get_pages()

def get_content(url,name):
    MarkdownExporter(block_url=url,output_path=folderpath,download=True, unzipped=True,output_filename=name).export()
    return

for page in pages:
    url = page["url"]
    name=page["properties"]["Name"]["title"][0]["plain_text"]
    get_content(url,name)

# MarkdownExporter will make markdown file on your output path

