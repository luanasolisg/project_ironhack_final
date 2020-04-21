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
    #browser.find_element_by_class_name('dy-lb-close').click()
# loop through all keys and search for them
    search_bar = browser.find_element_by_name("query")
    search_bar.send_keys(ean)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)
# go through all the search results per key and add them to the links_list
    titles_list = []
    prices_list = []
    try:
        item_titles = browser.find_element_by_xpath("//h1[@itemprop='name']").text
        for title in item_titles:
            titles_list.append(title)
        title = [item_titles]
        item_prices = browser.find_element_by_xpath("//meta[@itemprop='price']").get_attribute("content")
        prices_list.append(item_prices)
        price = prices_list
    except:
        titles_list.append('Alert')
        title = titles_list
        prices_list.append('None')
        price = prices_list
    df_msh = pd.DataFrame(zip(title, price), columns=["ItemName", "Price"])
    df_msh['Product'] = ean
    time.sleep(3)
    browser.find_element_by_name("query").clear()
    browser.close
    return df_msh

def m(product, url):
    browser_m = website(url)
    time.sleep(3)
    df_list = []
    for ean in product:
        m_df = titleslist(ean, browser_m)
        df_list.append(m_df)
    df_final = pd.concat(df_list)
    df_final['account']= 'M'
    df_final['date']= datetime.today().strftime('%Y-%m-%d')
    df_final.reset_index(inplace=True, drop=True)
    outpath = "C:/path"
    filename = 'M_'+(time.strftime("%Y%m%d")+".csv")
    df_final.to_csv(outpath + filename)
    return df_final