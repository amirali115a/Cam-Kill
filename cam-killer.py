import requests, re , colorama ,random
from requests.structures import CaseInsensitiveDict
from colorama import Fore
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--country", help="Specify the country for the generated data")

args = parser.parse_args()
country = args.country


headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
print("""
 ████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄█   ▄█▄  ▄█   ▄█        ▄█       
███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███ ▄███▀ ███  ███       ███       
███    █▀    ███    ███ ███   ███   ███   ███▐██▀   ███▌ ███       ███       
███          ███    ███ ███   ███   ███  ▄█████▀    ███▌ ███       ███       
███        ▀███████████ ███   ███   ███ ▀▀█████▄    ███▌ ███       ███       
███    █▄    ███    ███ ███   ███   ███   ███▐██▄   ███  ███       ███       
███    ███   ███    ███ ███   ███   ███   ███ ▀███▄ ███  ███▌    ▄ ███▌    ▄ 
████████▀    ███    █▀   ▀█   ███   █▀    ███   ▀█▀ █▀   █████▄▄██ █████▄▄██ 
                                          ▀              ▀         ▀         
""")
try:
   

    country =args.country
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
          for ip in find_ip:
           
              print(Fore.BLACK,"_____________________________________________________-")
                    
              print(Fore.GREEN, ip)
              f.write(f'{ip}\n')
except:
    pass
finally:
    print('')