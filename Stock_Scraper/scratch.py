from lxml import html
import requests
from bs4 import BeautifulSoup
import os
from argparse import ArgumentParser


    __APP_NAME = "Yahoo_Finance_Scraper"
    __VERSION = "0.0.1"
    __BASE_URL = "https://finance.yahoo.com/quote/{}"

    def __init__(self, item_name):
        self.item_name = item_name
        self.split_name = self.split_term()
        self.item_page = yahoo_finance_scraper.__BASE_URL.format(self.split_name)

        # Item specific
        self.page_markup = self.parse_page()
        self.listings = self.get_all_listings()
        self.number_of_listings = len(self.listings)
        self.item_list = []

        # HTML Output
        self.html_items = ""

    def split_term(self):
        print("Debug - splitting {}".format(self.item_name))
        st = self.item_name.replace(" ", "+")
        print("Debug - New search term: {}".format(st))
        return st

    def parse_page(self):
        # Scrape the website
        s = requests.get(self.item_page)
        if s:
            return s.text
        else:
            print("Exception - Unable to parse page!")

    def get_all_listings(self):
        soup = BeautifulSoup(self.page_markup, "lxml")


    print("Starting {} v({})".format(yahoo_finance_scraper.__APP_NAME, yahoo_finance_scraper.__VERSION))
    for item in self.listings:
        name = self.get_name(item)
        if name:
            price = self.get_price(item)
        if name and price:
            prod_url = self.get_prod_url(item)
            pic_url = self.get_image_url(item)
            self.item_list.append([name, price, pic_url, prod_url])

    if len(self.item_list) > 0:
        for p in self.item_list:
            self.html_items += ROW_TEMPLATE.format(p[0], "Ebay", p[1], p[2], p[3])

    print("{} complete!".format(yahoo_finance_scraper.__APP_NAME))


