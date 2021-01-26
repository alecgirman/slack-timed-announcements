## Slack announcement bot

This is a Slack bot to post announcements at certain times automatically.

### Installation

To use this on your own server, you must do the following:

1. Create an app in your slack server and register it as a bot.  This gives you the bot API token you will need later.

2. Create a .env file with `SLACK_API_TOKEN=<your bot API token>`

3. Create a config.json and populate it with channels.  It should look like this:

```json
"channels": {
    "general": "<channel ID for #general",
    "announcements": "<channel id for #announcements"
}
```
and then add channels that you would use in the format above.

4. Create an announcements.json with the following format:

```json
[
    {
        "channel": "general",
        "day": "Tuesday",
        "time": "220000",
        "message": "This is a test annoucement!"
    },
    {
        "channel": "bot-testing",
        "day": "Tuesday",
        "time": "223325",
        "message": "This is a multiline\nannouncement"
    }
]
```

where the `time` field is just the timestamp without the colons, `day` is the name of the day to post the announcement, and `channel` is the name of the channel that you used in channel.json.

### Manually send a message

To manually send a message in a channel, use the following command:

`python3 bot.py send general "message"`

Where `general` can be replaced with a name of a channel found in your channels.json.  It is important to include the quotes around the message.
