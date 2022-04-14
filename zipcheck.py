#find interesting things about a zip code
import requests
#import requests to get to our webapi
import json
#we expect json results. This will allow us to manipulte them as a dict

#define our values
ZIP_CODE = '73301'
COUNTRY = 'US'
# lets check that this is the zip for Austin.
CONTROL = 'Austinx'
# Use the Zippo public API


# this is our main testing function. Call with the Zip/Postcode, Country and control.
def CheckZipCity(zip,country,testvalue):
    webresponse = requests.get("http://api.zippopotam.us/"+ country + "/" + zip)
# verify we got a good response
    if webresponse.status_code !=200:
# if its not a 200 we have a website problem.
        print('site not responding')
        return False
        # send back a failure.        
    jsonresponse = json.loads(webresponse.content)
    # load up our response into a dictionary 
#ok we have a response lets parse it and verify the content against the control.
    if jsonresponse['places'][0]['place name'] == testvalue:
    #city match send it back with a success
        return True
    # No match return a failure. display api payload to console for debugging
    print(webresponse.content)
    return False


# Call the zip function with the control.
if CheckZipCity(ZIP_CODE,COUNTRY,CONTROL) == True:
        print('Control match')
else:
        print('Failed')
