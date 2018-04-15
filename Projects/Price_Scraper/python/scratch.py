from sample_page import sample
from bs4 import BeautifulSoup
import urllib.request
import time
import os
import sys
from html_writer import TEMPLATE, ROW_TEMPLATE

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
print(SCRIPT_DIR)
PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir)
print(PROJECT_ROOT)
BIN_ROOT = PROJECT_ROOT = os.path.normpath(SCRIPT_DIR + os.sep + os.pardir + os.sep + "bin")
print(BIN_ROOT)
HTML_ROOT = os.path.join(BIN_ROOT, "html")
print(HTML_ROOT)

# Parse the HTML markup
soup = BeautifulSoup(sample, "lxml")
# print(soup.find("a"))

"""
for product in soup.find_all('li'):  #li = List
    for img in product.find_all('img'):
        print("Name: {}".format(img.get("alt")))

for product in soup.find_all('span', {"class": "bold"}):
    print(product.getText().strip())
"""
all_products = soup.find_all('li')
number_of_products = len(all_products)
time.sleep(1)
master_list = []

product_number = 0
for product in all_products:  # li = List

    product_number += 1

    # Get name
    name = product.find('img')
    if name:
        name = name.get("alt").strip()
        #print("Name: {}".format(name))

    # Get price
    price = product.find('span', {"class": "bold"})
    if name and price:
        price = price.getText().strip()
        #print("Price: {}".format(price))

    # Get Product Link
    if name and price:
        product_link = product.find("a")
        prod_url = product_link.get('href')
        #print(prod_url)

    # Get Image Link
    if name and price:
        picture_link = product.find("img")
        pic_url = picture_link.get('src')
        #print(pic_url)

    # Download image
    #if name and price:
    #    print("Downloading picture for {}..".format(product_number))
    #    pic_name = "pic{}.jpg".format(product_number)
    #    pic_dir = os.path.join(BIN_ROOT, "pics", pic_name)
    #    urllib.request.urlretrieve(pic_url, pic_dir)
    #    print('\n')

    if name and price:
        master_list.append([name, price, pic_url, prod_url])

html_rows = ""
for p in master_list:
    html_rows += ROW_TEMPLATE.format(p[0], "Ebay", p[1], p[2], p[3])

html_rows.replace("\n", "")

print(html_rows)
#print(TEMPLATE.format(html_rows))


#output_html = HTML_ROOT + os.sep + "output.html"
#with open(output_html, "w") as writer:
#    writer.write(TEMPLATE.format(html_rows))


