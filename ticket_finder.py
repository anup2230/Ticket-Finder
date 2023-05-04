import os, requests, time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Seatgeek API Credentials
MYCLIENTID = "MjY4NzAwNDN8MTY4MDc2NDY4OS4zNDAyMTE"
MYCLIENTSECRET = "08344d82fc87139119f1f64716e1186caa6fea46897e21ca43603a2c0d34b761"

# Slack API Credentials
SLACK_BOT_TOKEN = 'xoxb-5220496871392-5196826432690-T94IN3pfcOWWGTMiabdxlh3H'
SLACK_CHANNEL_NAME = '#taylor-swift-ticket-finder'

artist = "taylor+swift"

URL = 'https://api.seatgeek.com/2/events?q={}&per_page=1000&client_id={}&client_secret={}'.format(artist, MYCLIENTID, MYCLIENTSECRET)

page = requests.get(URL)
result="Hello, world!"

while True: 
    
    page = requests.get(URL)
    page_json = page.json()['events']

    for i in range(len(page_json)):
        event_title = page_json[i]['short_title']
        lowest_price = page_json[i]['stats']['lowest_price']

        if event_title.startswith("Taylor Swift with") and (lowest_price <= 1200):
            print(event_title + ": Lowest Price = " + str(lowest_price))
            print(page_json[i]['url'])
    time.sleep(60)
