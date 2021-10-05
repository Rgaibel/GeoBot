from slack import WebClient
from geobot import GeoBot
import os

# Create a slack client
slack_web_client = WebClient(token="xoxb-1340711124560-1344053445169-MzLJEdMGa4ujbOOAAYyFTA30")

# Get a new CoinBot
coin_bot = GeoBot("channel")

# Get the onboarding message payload
message = coin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)