import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/46.0.2490.76 Mobile Safari/537.36'
}

destination_url = "https://www.tesla.com/findus/list/chargers/United+States"

destination_charger_data = requests.get(destination_url)
destination_soup = BeautifulSoup(destination_charger_data.text, "lxml")
all_states = destination_soup.find_all(class_="state")
# print(all_states[0].find("h2").text)
cali_info = [i for i in all_states if i.find("h2").text == "California"][0]
cali_hrefs = ["https://www.tesla.com" + i.get("href") for i in cali_info.find_all("a")]

waited_url = cali_hrefs
dest_detail_info = {}


def get_dest_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    area = soup.select("#find-us-list-container > div > header > h1")[0].text
    # seoncd_area = #find-us-list-container > div > header > h1
    chargers_des = "".join([i.text for i in soup.find_all("p") if "Connectors" in i.text])
    dest_detail_info.setdefault(chargers_des, "")
    chargers = catch_connectors(chargers_des)
    dest_detail_info[chargers_des] = chargers
    # if not area:
    #     print("{} has problem".format(url))
    # else:
    #     print([area, chargers])
    return [area, chargers]


def catch_connectors(des):
    connector_match = re.compile("(\d+) Tesla Connectors, up to (\d+kW)")
    chargers = re.findall(connector_match, des)
    return chargers


while len(waited_url) != 0:
    for i in waited_url:
        try:
            get_dest_info(i)
            print("success {}".format(i))
            del waited_url[i]
        except:
            # print("fail {}".format(i))
            pass

pprint(dest_detail_info)
