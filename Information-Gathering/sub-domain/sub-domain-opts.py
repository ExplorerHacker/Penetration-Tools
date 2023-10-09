# sub-domain crawler
import requests, termcolor
from datetime import datetime
from optparse import OptionParser


try:
    start=datetime.now()
    def main():
        parser = OptionParser()
        parser.add_option("-d", "--domain", dest="domain", help="Please specify domain.")
        parser.add_option("-f", "--file", 
                          action="store", 
                          dest="file", 
                          help="Please specify the file from it's path", 
                          metavar="FILE")
        (options, args) = parser.parse_args()
        if options.domain == None:
            return parser.error("Specify the domain (exp.host20.uk). Type -h to get help")
        elif options.file == None:
            return parser.error("Specify the file (path/*.txt). Type -h to get help")
        elif not options.domain and not options.file:
            return parser.error("Can't be empty. Type -h to get help")
        return options
      
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
                    
    else:
        print(termcolor.colored('[-] Domain is not registered!!!', 'red'))
    stop=datetime.now()

    totaltime=stop-start
    print(termcolor.colored("[***]TotalTimeTaken = ", 'yellow') + termcolor.colored(totaltime, 'grey'))
    
except KeyboardInterrupt:
    print(termcolor.colored('[-] Keyboard Interupted!!!', 'red'))
    
           