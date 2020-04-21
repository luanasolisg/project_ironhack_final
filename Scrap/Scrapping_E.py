#Web Scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import *
#Data manipulation
import pandas as pd
#time imports
import time
from datetime import datetime

def website(url):
    executable_path = r'C:\\path'
    # Select custom Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # Open the Chrome browser
    browser = webdriver.Chrome(executable_path, options = options)
    browser.get(url)
    return browser

def titleslist(ean, browser):
# loop through all keys and search for them
    search_bar = browser.find_element_by_id("search-box")
    search_bar.send_keys(ean)
    search_bar.send_keys(Keys.ENTER)
# go through all the search results per key and add them to the links_list
    titles_list = []
    prices_list = []
    try:
        item_titles = browser.find_elements_by_class_name("title")
        for title in item_titles:
            titles_list.append(title.text)
        title = [titles_list[0]]
        item_prices = browser.find_element_by_xpath("//span[@itemprop='price']").get_attribute("content")
        prices_list.append(item_prices)
        price = prices_list
    except:
        titles_list.append('Alert')
        title = titles_list
        prices_list.append('None')
        price = prices_list
    df_eci = pd.DataFrame(zip(title, price), columns=["ItemName", "Price"])
    df_eci['Product'] = ean
    time.sleep(3)
    browser.find_element_by_id("search-box").clear()
    browser.close
    return df_eci

def e(product, url):
    browser_e = website(url)
    time.sleep(3)
    df_list = []
    for ean in product:
        e_df = titleslist(ean, browser_e)
        df_list.append(e_df)
    df_final = pd.concat(df_list)
    df_final['account']= 'E'
    df_final['date']= datetime.today().strftime('%Y-%m-%d')
    df_final.reset_index(inplace=True, drop=True)
    outpath = "C:/path"
    filename = 'E_'+(time.strftime("%Y%m%d")+".csv")
    df_final.to_csv(outpath + filename)
    return df_final