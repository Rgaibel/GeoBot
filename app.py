import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from geobot import GeoBot

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injection.
slack_events_adapter = SlackEventAdapter("42b4c6ca3596bb05f534a6612bb36718", "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token="xoxb-1340711124560-1344053445169-MzLJEdMGa4ujbOOAAYyFTA30")

country_name = "not yet"


def winner(channel):
    # Create a new GeoBot
    geo_bot = GeoBot(channel)

    # Get the onboarding message payload
    message = geo_bot.get_message_winner()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


def loser(channel):
    global country_name
    # Create a new GeoBot
    geo_bot = GeoBot(channel)

    # Get the on boarding message payload
    message = geo_bot.get_message_loss(f"{country_name}")

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


def country_generator(channel):
    # Create a new CoinBot
    coin_bot = GeoBot(channel)

    # Get the onboarding message payload
    country = coin_bot.get_random_country()
    global country_name
    country_name = coin_bot.country
    message = coin_bot.get_message_picture()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


def flag_generator(channel):
    # Create a new CoinBot
    coin_bot = GeoBot(channel)

    # Get the onboarding message payload
    country = coin_bot.get_random_country()
    global country_name
    country_name = coin_bot.country
    message = coin_bot.get_message_flag(country)

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    global country_name

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if one of the activation phrases are in the text of the message.
    # If so, execute the corresponding code.
    if "countries" in text.lower():
        # Since the activation phrase was met, get the channel ID that the event
        # was executed on
        channel_id = event.get("channel")

        # return a picture of a country
        return country_generator(channel_id)
    elif "flags" in text.lower():
        # Since the activation phrase was met, get the channel ID that the event was executed on
        channel_id = event.get("channel")

        # return a flag of a country
        return flag_generator(channel_id)
    elif f"{country_name}" in text:
        # Since the activation phrase was met, get the channel ID that the event
        # was executed on
        channel_id = event.get("channel")

        # return a winning answer
        return winner(channel_id)
    for k in GeoBot.country_dict.keys():
        if k in text:
            channel_id = event.get("channel")

            # return disappointing answer
            return loser(channel_id)


if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='127.0.0.1', port=5000)
