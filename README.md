# Has my IP changed?

Small python script to determine a host's external IP and send a Slack bot message to the user whenever the IP changes.

If you have a home server and don't have a static IP from your ISP, then this script could be useful to always be able to find the server's location.
Ideally, this script would run regularly as a cronjob, e.g., once per day, on the server.


## Usage

1. This script requires Python >= 3.4. The only extra package required is [`slacker`](https://github.com/os/slacker), a Python interface to the Slack API (well, `slacker` has a few requirements itself): `pip install -r requirements.pip`

1. Copy the configurations template: `$cp config_template.py config.py`.
    This file will be ignore by git.

1. Create a Slack [User Token](https://api.slack.com/docs/token-types), if you don't already have one, and save it to `SLACK_TOKEN` variable in `config.py`: `SLACK_TOKEN = "<Your access token>"`.
    Alternatively you can use a [Test Token](https://api.slack.com/custom-integrations/legacy-tokens). **Warning:** Never publish your test tokens online!

1. Define the channel you want to receive the message. For example, to have the message appear in your own "slackbot" channel use: `CHANNEL = @<your-username>`

1. (Optional) Set up where in the disk the IP will be stored. By default IP is stored to `external_ip.txt` in the same directory.

1. (Optional) Customize your bot message (See below).

1. Run the script!

        $ ./has_my_ip_changed.py

    The first time it runs it will always Slack the user.


## Slack message

If you just configure the `SLACK_TOKEN` and `CHANNEL` variables then you get a message like this one:

![default](default_msg.png)

Everything in the message can be customized:

    # Customize your bot message with these optional configs
    BOTNAME = "Where am I now?"
    EMOJI = ":thinking_face:"

    # Message to the user that can, optionally display the new IP
    MSG_TEMPLATE = "Hey, I moved to:{ip}"

![custom](custom_msg.png)

See the `config_template.py` for the other configurations.


## Why Slack?

Really I just thought I would be fun to get these messages on my Slack. Besides, the ability to customize your bot's name and emoji makes for some fun messaging :grinning:

Still, if you prefer email, then all you would have to do is replace the contents of `slack_user()` with the appropriate code for one of the many 3rd-party email APIs like [Mailgun](https://www.mailgun.com/) or [yagmail](https://github.com/kootenpv/yagmail).
