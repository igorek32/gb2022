####################### Файл main.py
import requests
from datetime import datetime
import utils
import sys
name = input('Напечатайте название валюты: ').upper()
#name = sys.argv[1].upper()раскментить для задания 5, закоментив верхнюю строку
value,date = utils.converter(name)

print(value, ' ', date)

####################### Файл utils.py
import requests
from datetime import datetime

def converter(name):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    data = str(requests.get(url).content)
    try:
        value = float((((data.split(name)[1]).split("<Value>")[1]).split("<")[0]).replace(",","."))
    except:
        value = None
    date = ((data.split('Date="')[1]).split('" ')[0]).replace(".","-")
    return value,date

