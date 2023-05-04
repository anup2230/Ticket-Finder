import os, requests, time


# Seatgeek API Credentials
MYCLIENTID = "MjY4NzAwNDN8MTY4MDc2NDY4OS4zNDAyMTE"
MYCLIENTSECRET = "08344d82fc87139119f1f64716e1186caa6fea46897e21ca43603a2c0d34b761"

#Discord Data to Send
payload = {
    'content' : "hello"
}
#Discord Auth
header = {
    'authorization' : "Mzk4NjgzMDkxMjM0OTc5ODUy.G2cqyG.zefXL2zo4vGVYNh38IVFcdGKtO5GPy--DAdEiU"
}

#artist to search for
artist = "taylor+swift"

#API CALL URL
URL = 'https://api.seatgeek.com/2/events?q={}&per_page=1000&client_id={}&client_secret={}'.format(artist, MYCLIENTID, MYCLIENTSECRET)

page = requests.get(URL)
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

        if event_title.startswith("Taylor Swift with") and (lowest_price <= 1150):
            payload['content'] = event_title + ": Lowest Price = " + str(lowest_price) + " , " + venue + " | " + city + "\n" + event['url']
            requests.post("https://discord.com/api/v9/channels/1103593266189975625/messages", data=payload, headers=header)
            print(payload['content'])
    time.sleep(60)
