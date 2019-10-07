from xmljson import BadgerFish
from xml.etree.ElementTree import fromstring
import urllib.request
from datetime import date
import os.path
import load_config

bf = BadgerFish(dict_type=dict)
config = load_config.load('config.yaml') 

url = config["convertPriceURL"]
date = date.today().strftime("%Y-%m-%d")
xml_file_name = "data/"+date+"-convert-values.xml"

def download_latest_xml(url, xml_file_name= xml_file_name):
    urllib.request.urlretrieve(url, xml_file_name)

def check_existing_xml_and_download_latest_xml(url = url, xml_file_name = xml_file_name):
    print(xml_file_name)
    if not os.path.exists(xml_file_name):
        download_latest_xml(url, xml_file_name)

def load_raw(file_name = xml_file_name):
    with open(file_name,'r') as stream:
        return bf.data(fromstring(stream.read()))

def load(file_name = xml_file_name):
    return load_raw()[config["xmlRoot1"]][config["xmlRoot2"]][config["xmlRoot3"]]

if __name__ == "__main__":
    check_existing_xml_and_download_latest_xml()
    print(load())