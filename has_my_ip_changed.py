#!/usr/bin/env python
"""
Sends a Slack notification with the host's latest external IP.
Ideally, this script is run regularly as a cronjob, e.g., once per day.
"""
import subprocess
import shlex
import sys
from pathlib import Path

from slacker import Slacker

import config
# try:
# except ImportError:
#     # dummy object if config.py doesn't exist
#     # See config_template.py for example configuration
#     config = object()


def get_ip():
    """
    Use a DNS server to get the host's external IP.
    """
    # https://unix.stackexchange.com/a/81699
    cmd = "dig +short myip.opendns.com @resolver1.opendns.com"

    proc = subprocess.Popen(
        shlex.split(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = proc.communicate()

    if err:
        raise ValueError(err.decode().strip())
    return out.decode().strip()


def save_ip(fp, ip):
    """
    Save the IP to the location of the given Path object.
    """
    with fp.open("w") as f:
        f.write(ip)


def slack_user(ip):
    """
    Send a slack message to the user with the new IP.
    """

    slack_token = getattr(config, "SLACK_TOKEN")
    channel = getattr(config, "CHANNEL")
    botname = getattr(config, "BOTNAME", None)
    emoji = getattr(config, "EMOJI", None)

    # Message to the user that can, optionally display the new IP
    msg_template = getattr(config, "MSG_TEMPLATE", "{ip}")
    msg = msg_template.format(ip=ip)

    slack = Slacker(slack_token)
    slack.chat.post_message(
        channel, msg, username=botname, icon_emoji=emoji
    )


def main():
    try:
        new_ip = get_ip()
    except ValueError as e:
        print("Error while checking IP:", e)
        return 1

    print("Current IP is:", new_ip)

    ip_file = Path(getattr(config, "IP_FILEPATH", "external_ip.txt"))
    # First time running the script?
    if not ip_file.is_file():
        print("First time running!")
        print("Saving latest IP to", ip_file, "and notifying user.")
        save_ip(ip_file, new_ip)
        slack_user(new_ip)
        return 0
    # File exists, let's compare the IPs
    else:
        with ip_file.open() as f:
            previous_ip = f.read().strip()

        if previous_ip != new_ip:
            print("IP has changed:", previous_ip, "-->", new_ip)
            print("Saving new IP to", ip_file, "and notifying user.")
            save_ip(ip_file, new_ip)
            slack_user(new_ip)
        else:
            print("No change.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
