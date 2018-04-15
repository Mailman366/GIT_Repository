from lxml import html
import requests
from bs4 import BeautifulSoup
import os
from argparse import ArgumentParser

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir)
BIN_ROOT = PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir + os.sep + "bin")
HTML_ROOT = os.path.join(BIN_ROOT, "html")
OUTPUT_HTML = output_html = HTML_ROOT + os.sep + "output.html"


class yahoo_finance_scraper(object):
    """
    Scrapes information from Yahoo Finance
    """

    __APP_NAME = "Yahoo_Finance_Scraper"
    __VERSION = "0.0.1"
    __BASE_URL = "https://finance.yahoo.com/quote/{}"

    def __init__(self, ticker):
        self.ticker = ticker
        self.item_page = yahoo_finance_scraper.__BASE_URL.format(self.ticker)

        # Item specific
        self.page_markup = self.parse_page()
        self.page = self.get_all_listings()


        # HTML Output
        self.html_items = ""

    def parse_page(self):
        # Scrape the website
        s = requests.get(self.item_page)
        if s:
            return s.text
        else:
            print("Exception - Unable to parse page!")

    def get_all_listings(self):
        soup = BeautifulSoup(self.page_markup, "lxml")
        return soup

    def get_current_price(self, listing):
        url = listing.find("regularMarketChange")
        return url

    def main(self):

        print("Starting {} v({})".format(yahoo_finance_scraper.__APP_NAME, yahoo_finance_scraper.__VERSION))
        #print(self.page_markup)
        print(self.get_current_price(self.page))
        print("{} complete!".format(yahoo_finance_scraper.__APP_NAME))



def parse_args():
    p = ArgumentParser()
    p.add_argument("-t", "--ticker", type=str, required=True)
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    a = yahoo_finance_scraper(args.ticker)
    a.main()


    print("Complete!")
