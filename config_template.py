"""
User configuration template

Usage:
    1. `cp config_template.py config.py`
    2. Make any necessary changes to config.py

Contains tokens and usernames so, KEEP THIS FILE OUT OF VERSION CONTROL.
"""

# Where in the disk to store the IP
IP_FILEPATH = "external_ip.txt"

# Slack User Token
# How to get a User Token: https://api.slack.com/docs/token-types
# Users can also generate test tokens this way:
# https://api.slack.com/custom-integrations/legacy-tokens
# NEVER PUBLISH YOUR TEST TOKENS ONLINE
SLACK_TOKEN = "<Your access token>"

# Where to send the message
# Use @<your username> to send the message to the "slackbot" channel
CHANNEL = "@username"

# Customize your bot message with these optional configs
BOTNAME = "Where am I now?"
EMOJI = ":thinking_face:"

# Message to the user that can, optionally display the new IP
MSG_TEMPLATE = "Hey, I moved to:{ip}"
