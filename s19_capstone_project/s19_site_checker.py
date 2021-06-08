# File name: siteChecker.py
# Description:  Check if the web page is alive at regular intervals
# Author: Juris Tihomirovs
# Date: 04-06-2021
import time

import requests
from colorama import Fore

url = 'https://www.delfi.lv/'
start_time = time.time()

while True:
    page = requests.get(url)

    if page.ok:
        print(Fore.GREEN + f'{time.ctime()}: {page.status_code} OK')
    else:
        print(Fore.RED + f'{time.ctime()}: {page.status_code} NOK')

    # Repeat after minute
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))
