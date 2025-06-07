import requests
import time
from fake_useragent import UserAgent
url = "https://www.flipkart.com/search?q=earbuds&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&as-pos=3&as-type=RECENT&suggestionId=earbuds&requestId=d2f75bef-aea0-4a10-8174-41196132f422&as-backfill=on"



session = requests.Session()
headers = {
    "User-Agent": UserAgent().random,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com",   
}
time.sleep(15)

r = session.get(url, headers=headers, cookies=session.cookies)
print(r.status_code)

with open("flipkart1.html", "w", encoding="utf-8") as f:
    f.write(r.text)