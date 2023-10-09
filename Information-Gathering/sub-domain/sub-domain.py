# sub-domain crawler
import requests, termcolor
from datetime import datetime



start=datetime.now()

try:
    target_domain = input(termcolor.colored("Enter domain name: ", "green"))
    print(termcolor.colored("You are crawling ", 'yellow') + termcolor.colored(target_domain, 'grey'))

    def discover_subdomain(domain):
        try:
            if 'http://'+ domain:
                return requests.get("http://" + domain)
            elif 'https://'+domain:
                return requests.get("https://" + domain)
            else:
                pass
        except requests.exceptions.ConnectionError:
            pass
        except TypeError:
            print(termcolor.colored('[-] Type Error!!!. Please check enter correct domain!!', 'red'))

    if discover_subdomain(target_domain):	
        with open("subdomains-100.txt", "r") as wordlist_file:
            for line in wordlist_file:
                subs = line.strip()
                result = subs + "." + target_domain
                resultUrl = discover_subdomain(result)
                res = discover_subdomain(result)
                if res:
                    print(termcolor.colored("[+] Discover subdomain ==> ", 'green') + termcolor.colored(result, 'blue') + '    ' + termcolor.colored(resultUrl.url, 'blue'))
                    
    else:
        print(termcolor.colored('[-] Domain is not registered!!!', 'red'))
    stop=datetime.now()

    totaltime=stop-start
    print(termcolor.colored("[***]TotalTimeTaken = ", 'yellow') + termcolor.colored(totaltime, 'grey'))
    
except KeyboardInterrupt:
    print(termcolor.colored('[-] Keyboard Interupted!!!', 'red'))
    
    