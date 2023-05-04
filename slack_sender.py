import os, requests, time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Seatgeek API Credentials
MYCLIENTID = "MjY4NzAwNDN8MTY4MDc2NDY4OS4zNDAyMTE"
MYCLIENTSECRET = "08344d82fc87139119f1f64716e1186caa6fea46897e21ca43603a2c0d34b761"

# Slack API Credentials
SLACK_BOT_TOKEN = 'xoxb-5220496871392-5196826432690-fjtvtMid6NiDZbCRQZpdVhJ8'
SLACK_CHANNEL_NAME = '#taylor-swift-ticket-bot'

artist = "taylor+swift"

URL = 'https://api.seatgeek.com/2/events?q={}&per_page=1000&client_id={}&client_secret={}'.format(artist, MYCLIENTID, MYCLIENTSECRET)

page = requests.get(URL)
client = WebClient(token=SLACK_BOT_TOKEN)
result = ""

while True: 
    page = requests.get(URL)
    page_json = page.json()['events']

    for i in range(len(page_json)):
        event = page_json[i]
        event_title = event['short_title']
        lowest_price = event['stats']['lowest_price']
        venue = event['venue']['name']
        city = event['venue']['city']

        if event_title.startswith("Taylor Swift with") and (lowest_price <= 1200):
            result = event_title + ": Lowest Price = " + str(lowest_price) + venue + "|" + city + "\n" + event['url']
            try:
                response = client.chat_postMessage(
                    channel=SLACK_CHANNEL_NAME,
                    text=result
                )
                print("Message sent: ", response["ts"])  # ts is the timestamp of the message
            except SlackApiError as e:
                print("Error sending message: {}".format(e))
            print(result)
        time.sleep(1)    
    time.sleep(120)
