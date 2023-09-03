import phonenumbers, os, requests
from flask import Flask, render_template, request
from phonenumbers.util import prnt
from phonenumbers import geocoder, carrier, timezone
from myanmar.phonenumber import get_landline_operator, get_phone_operator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


app = Flask(__name__)

@app.route('/information-gathering/phone-number', methods=['GET', 'POST'])
def phoneGath():
    phonenumber = ''
    ccnn = ''
    geol = ''
    carrie = ''
    timezn = ''
    region = ''
    whatNum = ''
    user = os.environ.get('USERNAME')
    
    if request.method == "POST":
        phonenumber = request.form['phonenumber']
        try:
            ccnn = phonenumbers.parse(phonenumber)
            geol = geocoder.description_for_number(ccnn, "en")
            timezn = timezone.time_zones_for_number(ccnn)
            carrie = carrier.name_for_number(ccnn, "en")
            region = phonenumbers.region_code_for_number(ccnn)

            what = f"https://wa.me/{phonenumber}"
            # what = f"https://api.whatsapp.com/send?phone={phonenumber}&text=hello."
            res = requests.head(what)
            print(res)
        except phonenumbers.phonenumberutil.NumberParseException:
            ccnn = "Error on NumberParseException. Please include country code!!! e.g (+1, +44 etc)"
    return render_template('Information-Gathering/pho-number.html', 
                           phonenumber = phonenumber, 
                           user = user, 
                           ccnn = ccnn,
                           geol = geol,
                           carrie = carrie,
                           timezn = timezn,
                           region = region,
                           whatNum = whatNum,
                        )

@app.route('/information-gathering', methods=['GET', 'POST'])
def infoGath():
    return render_template('Information-Gathering/index.html')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug = True)
    