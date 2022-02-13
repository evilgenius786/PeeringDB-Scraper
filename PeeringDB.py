import json
import os.path
import traceback

import requests
from bs4 import BeautifulSoup

scriptsdir = "./scripts"
urls = ["https://www.peeringdb.com/ix/3431"]

def main():
    logo()
    if not os.path.isdir(scriptsdir):
        os.mkdir(scriptsdir)
    for url in urls:
        print("Working on URL", url)
        try:
            soup = BeautifulSoup(requests.get(url).content, 'lxml')
            # print(soup)
            filename = f"{soup.find('div', {'data-edit-name': 'name'}).get('data-edit-value')}-{url.split('/')[-1]}.sh"
            out = ""
            for row in soup.find('div', {'id': "list-networks"}).find_all('div', {"class": "row item operational"}):
                data = {
                    'ASN': row.find('div', {"class": "asn"}).text.strip(),
                    'IP4': row.find('div', {"class": "ip4"}).text.strip(),
                    'IP6': row.find('div', {"class": "ip6"}).text.strip(),
                    'Peer': row.find('div', {"class": "peer"}).text.strip(),
                }
                print(json.dumps(data,
                                 # indent=4
                                 ))

        except:
            print("Error on", url)
            traceback.print_exc()


def logo():
    os.system('color 0a')
    print(r"""
    __________                    .__              ________ __________ 
    \______   \ ____   ___________|__| ____    ____\______ \\______   \
     |     ___// __ \_/ __ \_  __ \  |/    \  / ___\|    |  \|    |  _/
     |    |   \  ___/\  ___/|  | \/  |   |  \/ /_/  >    `   \    |   \
     |____|    \___  >\___  >__|  |__|___|  /\___  /_______  /______  /
                   \/     \/              \//_____/        \/       \/ 
============================================================================
            Script generator and scraper from PeeringDB by:
                   http://github.com/evilgenius786
============================================================================
[+] Without browser
[+] With error handling
[+] Show results in logs
____________________________________________________________________________
""")


if __name__ == '__main__':
    main()
