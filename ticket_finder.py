import os, requests, time



def find_tickets():
    MYCLIENTID = "MjY4NzAwNDN8MTY4MDc2NDY4OS4zNDAyMTE"
    MYCLIENTSECRET = os.environ.get("SEATGEEK_SECRET")
    artist = "taylor+swift"
    URL = 'https://api.seatgeek.com/2/events?q={}&per_page=400&client_id={}&client_secret={}'.format(artist, MYCLIENTID, MYCLIENTSECRET)


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

            if event_title.startswith("Taylor Swift") and (lowest_price <= 1000):
                result += event_title + ": Lowest Price = " + str(lowest_price) + " , " + venue + " | " + city + "\n" + event['url']
        if result == "": return "No Tickets Found Under the Criteria"
        else: return(result)
find_tickets()
