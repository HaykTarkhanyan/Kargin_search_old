"""
Code for scraping a Youtube playlist
and collecting video links and titles
"""


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def get_links(playlist):
    """
    Returns a dataframe of sketch titles with
    corresponding links given the playlist link.
    """

    data = pd.DataFrame()
    titles = []
    links = []

    print("Starting driver")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(playlist)

    print("Page opened")
    time.sleep(5)

    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(5)

    print("Getting titles")
    titles_selection = driver.find_elements_by_id("video-title")
    for title in titles_selection:
        titles.append(title.text)
    print (f"Videos found: {len(titles)}")
    data["titles"] = titles
    
    print("Getting links")
    links_selection = driver.find_elements_by_id("thumbnail")
    for link in links_selection[2::2]:
        links.append(link.get_attribute("href"))
    data["links"] = links

    return data
