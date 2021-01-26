from slack_sdk import WebClient
from time import sleep
from dotenv import load_dotenv
from envs import env
from sys import argv
import json

config = json.load(open("config.json", "r"))
announcements = json.load(open("announcements.json", "r"))
channels = config["channels"]

load_dotenv()
token = env("SLACK_API_TOKEN")

client = WebClient(token)


def make_announcement(channel, message):
    channel_id = channels[channel]
    client.chat_postMessage(channel=channel, text=message)


# manually send a message to a channel (like a management command)
if len(argv) > 1 and argv[1] == "send":
    make_announcement(argv[2], argv[3])
    exit(0)

while True:
    timestr = datetime.now().strftime("%H%M%S")
    daystr = datetime.now().strftime("%A")

    for ann in announcements:
        if ann["time"] == timestr and ann["day"] == daystr:
            make_announcement(ann["channel"], ann["message"])

    sleep(1)
