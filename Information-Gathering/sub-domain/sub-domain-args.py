# sub-domain crawler
import requests, termcolor, argparse
from datetime import datetime


try:
    start=datetime.now()
    
    def main():
        import argparse

        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument("-d", "--domain", dest="domain", help="Please specify domain.")
        parser.add_argument("-f", "--file",
                            # default="subdomains-100.txt",
                            dest="file",
                            help="Please specify the file from it's path",
                            metavar="FILE")

        args = parser.parse_args()
        if args.domain == None:
            return parser.error("Specify the domain (exp.host20.uk)")
        elif args.file == None:
            return parser.error("Specify the file (path/*.txt)")
        elif not args.domain and not args.file:
            return parser.error("Can't be empty. Type -h to get help")
        return args
        
    options = main()
    
    print('\t\t\t\t' + termcolor.colored("You are crawling ", 'yellow') + termcolor.colored(options.domain, 'grey'))

    def discover_subdomain(domain):
        try:
            if 'http://'+domain:
                return requests.get("http://" + domain)
            elif 'https://'+domain:
                return requests.get("https://" + domain)
            else:
                pass
        except requests.exceptions.ConnectionError:
            pass
        except TypeError:
            print(termcolor.colored('[-] Type Error!!!. Please check enter correct domain!!', 'red'))
    
    if discover_subdomain(options.domain):	
        with open(options.file, "r") as wordlist_file:
            for line in wordlist_file:
                subs = line.strip()
                result = subs + "." + options.domain
                resultUrl = discover_subdomain(result)
                res = discover_subdomain(result)
                if res:
                    print(termcolor.colored("[+] Discover subdomain ==> ", 'green') +  '\t' + termcolor.colored(result, 'blue') + '\t' + termcolor.colored(resultUrl.url, 'blue'))
                    
    stop=datetime.now()

    totaltime=stop-start
    print(termcolor.colored("[***]TotalTimeTaken = ", 'yellow') + termcolor.colored(totaltime, 'grey'))
    
except KeyboardInterrupt:
    print(termcolor.colored('[-] Keyboard Interupted!!!', 'red'))
    
           