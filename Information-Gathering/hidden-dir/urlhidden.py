import requests, termcolor, http.client
from datetime import datetime

# 192.168.234.132

try:
    targetUrl = input("URL> ")
    def geturl(domain):
        try:
            if domain.startswith("http://"):
                return requests.get(domain)
            elif domain.startswith('https://'):
                try:
                    return requests.get(domain)
                except requests.exceptions.ConnectionError:
                    print("URL invalid!!!")
                except requests.exceptions.InvalidURL:
                    print("Please enter valid input!!!")
            return requests.get(domain)
        except requests.exceptions.MissingSchema:
            try:
                url = 'https://' + domain
                print(url)
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                url = "http://" + domain
                print(url)
                return requests.get(url)
            except requests.exceptions.InvalidURL:
                print("Please enter valid input!!!")
        except requests.exceptions.ConnectionError:
            print("Remote https instead!!!")
        except requests.exceptions.InvalidURL:
            print("Please enter valid input!!!")
    get = geturl(targetUrl)
    if get:
        print(get)
except KeyboardInterrupt:
    print(termcolor.colored("[-] KeyboardInterrupted!!!", "red"))