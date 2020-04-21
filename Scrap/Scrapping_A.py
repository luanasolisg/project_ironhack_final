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
def a(url_list):
    executable_path=r'C:\\path'
    # Select custom Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # Open the Chrome browser
    browser = webdriver.Chrome(executable_path, options = options)
    df_list = []
    for url in url_list:
        browser.get(url)
        time.sleep(5)
        titles_list = []
        prices_list = []
        try:
            item_titles = browser.find_elements_by_class_name("a-size-large")
            for title in item_titles:
                titles_list.append(title.text)
            title = [titles_list[0]]
            item_prices = browser.find_elements_by_class_name("a-color-price")
            for price in item_prices:
                prices_list.append(price.text)
            price = [prices_list[0]]
        except:
            titles_list.append('Alert')
            title = titles_list
            prices_list.append('None')
            price = prices_list
        df_a = pd.DataFrame(zip(title, price), columns=["ItemName", "Price"])
        df_a['Product'] = '-'
        df_list.append(df_a)
    df_final = pd.concat(df_list)
    df_final['account']= 'A'
    df_final['date']= datetime.today().strftime('%Y-%m-%d')
    df_final.reset_index(inplace=True, drop=True)
    time.sleep(3)
    browser.close
    outpath = "C:/path"
    filename = 'A_'+(time.strftime("%Y%m%d")+".csv")
    df_final.to_csv(outpath + filename)
    return df_final
