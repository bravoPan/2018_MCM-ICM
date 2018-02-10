from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://www.tesla.com/findus/list/superchargers/United+States"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, "lxml")
state_list = soup.find_all(class_="state")

station_dict = {}

for i in state_list:
    # print(i)
    print(i.select("div > h2"))

