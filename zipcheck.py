#find interesting things about a zip code
import requests
#import requests to get to our webapi
ZIP_CODE = '73301'
COUNTRY = 'US'
CONTROL = 'Austin'
# lets check that this is the zip for Austin.
# Use the Zippo public API


def checkzipcity(zip,country,test):
    webresponse = requests.get("http://api.zippopotam.us/"+ COUNTRY + "/" + ZIP_CODE)