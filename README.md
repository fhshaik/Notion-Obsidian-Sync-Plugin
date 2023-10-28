# Notion-Obsidian-Sync-Plugin
Syncs Notion Files to an Obsidian Folder(one way) using an Obsidian.md Plugin

For the plugin to work you must place notion-sync folder into the plugins folder in your vault. 

You must also install the following packages for python which you can do using pip:


$ pip install requests

$ pip install notion2md


You must input the following data into the data.json for it to work:

NOTION_TOKEN: "Your Notion Token which you can get from website"

DATABASE_ID: "Name of Database you want to sync"

SYNC_FOLDER: "Which folder in obsidian do you want notion files to be downloaded to"


Two-way sync is a work in progress

