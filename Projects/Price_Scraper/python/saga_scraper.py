
import os
import sys
from ebay_price_scraper import ebay_scraper


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir)
BIN_ROOT = PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir + os.sep + "bin")
HTML_ROOT = os.path.join(BIN_ROOT, "html")


if __name__ == "__main__":
    es = ebay_scraper("Vintage Hulk Action Figure")
    es.main()
    sys.exit(0)