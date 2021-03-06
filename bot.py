from slack_sdk import WebClient
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from envs import env
from sys import argv
import json
import requests

config = json.load(open("config.json", "r"))
channels = config["channels"]

load_dotenv()
token = env("SLACK_API_TOKEN")
update_interval = env("UPDATE_INTERVAL", var_type="integer")
api_url = env("API_URL")
client = WebClient(token)


def make_announcement(channel, message):
    channel_id = channels[channel]
    client.chat_postMessage(channel=channel, text=message)


def read_announcements():
    response = requests.get(api_url)

    if response.status_code == 200:
        content = response.content.decode("utf-8")
        return json.loads(content)
    else:
        print(f"Error in retrieving announcements, status code {response.status_code}")


# manually send a message to a channel (like a management command)
if len(argv) > 1 and argv[1] == "send":
    make_announcement(argv[2], argv[3])
    exit(0)

announcements = read_announcements()
counter = 0
while True:
    timestr = datetime.now().strftime("%H%M%S")
    daystr = datetime.now().strftime("%A")

    for ann in announcements:
        ann["time"] = ann["time"].replace(":", "")
        if ann["time"] == timestr and ann["day"] == daystr:
            make_announcement(ann["channel"], ann["message"])

    sleep(1)
    counter = counter + 1

    if counter % update_interval == 0:
        announcements = read_announcements()
