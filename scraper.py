#current output: [('121,99', '121,99', ''), ('1', '1', ''), ('122,62', '122,62', '')]

from urllib.request import urlopen
import re

link = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=StatTrak%E2%84%A2%20M4A1-S%20|%20Hyper%20Beast%20(Minimal%20Wear)"
f = urlopen(link)
myfile = f.read().decode('utf-8')
f.close()

reg = re.findall("[+-]?((\d+\,?\d*)|(\,\d+))", myfile)
print(reg)