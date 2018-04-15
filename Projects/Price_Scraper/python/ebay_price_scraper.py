from lxml import html
import requests
import requests
import argparse
from pprint import pprint
import csv
from traceback import format_exc
import argparse
from bs4 import BeautifulSoup
from sample_page import sample
from bs4 import BeautifulSoup
import urllib.request
import time
import os
import sys
from html_writer import TEMPLATE, ROW_TEMPLATE, write_ebay_page, row_formatter

"""
TODO:
Name
Price
Length of Auction
Picture of Item
URL
"""

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir)
BIN_ROOT = PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir + os.sep + "bin")
HTML_ROOT = os.path.join(BIN_ROOT, "html")
OUTPUT_HTML = output_html = HTML_ROOT + os.sep + "output.html"


class ebay_scraper(object):
    """
    Scrapes information from Ebay html markups
    """

    __APP_NAME = "ebay_scraper"
    __VERSION = "0.0.1"
    #__BASE_URL = 'http://www.ebay.com/sch/i.html?_nkw={0}&_sacat=0'
    __BASE_URL = "https://www.ebay.com/csc/i.html?_sacat=0&_nkw={}"

    def __init__(self, item_name):
        self.item_name = item_name
        self.split_name = self.split_term()
        self.item_page = ebay_scraper.__BASE_URL.format(self.split_name)

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
        return soup.find_all('li')

    def get_name(self, listing):
        name = listing.find('img')
        if name:
            return name.get("alt").strip()

    def get_price(self, listing):
        price = listing.find('span', {"class": "bold"})
        if price:
            return price.getText().strip()

    def get_prod_url(self, listing):
        url = listing.find("a")
        return url.get('href')

    def get_image_url(self, listing):
        url = listing.find("img")
        return url.get('src')

    def main(self):

        print("Starting {} v({})".format(ebay_scraper.__APP_NAME, ebay_scraper.__VERSION))
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


        formatted_html = row_formatter(self.html_items)
        write_ebay_page(formatted_html, output_html)
        print("{} complete!".format(ebay_scraper.__APP_NAME))
