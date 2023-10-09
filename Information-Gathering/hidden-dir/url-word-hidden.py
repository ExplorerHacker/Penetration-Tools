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
                    print(termcolor.colored("[-] URL invalid!!!", "red"))
                except requests.exceptions.InvalidURL:
                    print(termcolor.colored("[-] Please enter valid input!!!", "red"))
            return requests.get(domain)
        except requests.exceptions.MissingSchema:
            try:
                url = 'https://' + domain
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                url = "http://" + domain
                return requests.get(url)
            except requests.exceptions.InvalidURL:
                print(termcolor.colored("[-] Please enter valid input!!!", "red"))
        except requests.exceptions.ConnectionError:
            print(termcolor.colored("[-] Use https instead!!!", "red"))
        except requests.exceptions.InvalidURL:
            print(termcolor.colored("[-] Please enter valid input!!!", "red"))
    get = geturl(targetUrl)
    if get:
        print(get.url)
        with open('filesdirswordlist.txt', 'r') as word:
            for w in word:
                line = w.strip()
                Urlpath = get.url + line
                res = geturl(Urlpath)
                
                if res.status_code == 200:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 201:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 203:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 204:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 205:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 206:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 207:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 209:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 301:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 302:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 303:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 304:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 305:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 306:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 307:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 309:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 401:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 402:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 403:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 405:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 406:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 407:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 501:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 502:
                    print(res.url, ' ', res.status_code)
                elif res.status_code == 503:
                    print(res.url, ' ', res.status_code)
except KeyboardInterrupt:
    print(termcolor.colored("[-] KeyboardInterrupted!!!", "red"))