import requests, socket
from whois import whois
from termcolor import colored

try:
  domain = input("[+] Enter Your Target Domain Name or IP domain: ")

  def get_ip_address(url):
    try:
      ip_address = socket.gethostbyname(url)
      return ip_address
    except socket.gaierror:
      return None
    
  ip_address = get_ip_address(domain)

  if ip_address:
    print(colored("[+] ", "yellow") + colored(f"The IP address of {domain} is: ", 'cyan') + colored(ip_address, 'blue'))
  else:
    print(f"Unable to resolve the IP address for {domain}")

  def add_http_if_missing(url):
    if not url.startswith('http://') and not url.startswith('https://'):
      return 'http://' + url
    return url

  def check_domain(url):
    try:
      return requests.get(add_http_if_missing(url))
    except requests.exceptions.ConnectTimeout:
      print(colored("[-] ", 'yellow') + colored("ConnectTimeoutError", 'red'))

  get = check_domain(domain)


  if bool(get) == True:
    print(colored("✔️✔️✔️  ", "yellow") + colored(domain, "blue") + colored(" is registered", "cyan"))
    def checkwhois(dname):
      return whois(dname)
    print(colored('[+] ', 'yellow') + colored('URL link >>> ', 'cyan') + colored(get.url, 'blue'))
    getH = checkwhois(get.url)
    print("""
          Enum Whois
                by: Nurudeen O.A 
                    Explorer
          """)
    print(colored("[+] ", "yellow") + colored("Domain Name >>> ", "cyan") + colored(getH.domain_name, 'blue'))
    print(colored("[+] ", "yellow") + colored("Registrar >>> ", "cyan") + colored(getH.registrar, 'blue'))
    print(colored("[+] ", "yellow") + colored("Whois Server >>> ", "cyan") + colored(getH.whois_server, 'blue'))
    print(colored("[+] ", "yellow") + colored("Referral url >>> ", "cyan") + colored(getH.referral_url, 'blue'))
    print(colored("[+] ", "yellow") + colored("DNS SEC at >>> ", "cyan") + colored(getH.dnssec, 'blue'))
    print(colored("[+] ", "yellow") + colored("Name >>> ", "cyan") + colored(getH.name, 'blue'))
    print(colored("[+] ", "yellow") + colored("Org >>> ", "cyan") + colored(getH.org, 'blue'))
    print(
          colored("[+] ", "yellow") + 
          colored("Address >>> ", "cyan") + 
          colored(getH.address , 'blue') + ', ' +
          colored(getH.city , 'blue') + ', ' +
          colored(getH.state , 'blue') + ', ' +
          colored(getH.registrant_postal_code , 'blue') + ', ' +
          colored(getH.country , 'blue')
        )
    print(colored("[+] ", "yellow") + colored("Updated date >>> ", "cyan") + colored(getH.updated_date, 'blue'))
    print(colored("[+] ", "yellow") + colored("Name servers >>> ", "cyan") + colored(getH.name_servers, 'blue'))
    print(colored("[+] ", "yellow") + colored("Status >>> ", "cyan") + colored(getH.status, 'blue'))
    print(colored("[+] ", "yellow") + colored("Emails >>> ", "cyan") + colored(getH.emails, 'blue'))

  else:
    print(domain, "is not registered")
except KeyboardInterrupt:
  print("KeyboardInterrupt!!!")
  