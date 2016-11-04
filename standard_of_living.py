# http://zipwho.com/
# https://www.irs.gov/uac/soi-tax-stats-individual-income-tax-statistics-2014-zip-code-data-soi
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

def mean_income(zip_code):
    url = "http://zipwho.com/?zip={0}&city=&filters=--_--_--_--&state=&mode=zip".format(zip_code)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    # txt = soup.findAll('td')
    txt = soup.select('.split')
    print(txt)

    # zest = ''
    # for script in txt:
    #     if script.has_attr('data-property-value'):
    #         zest = script['data-property-value']
