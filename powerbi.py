import bme280

import urllib, urllib2, time

from datetime import datetime

# REST API endpoint, given to you when you create an API streaming dataset

# Will be of the format: https://api.powerbi.com/beta//datasets/< dataset id>/rows?key=

REST_API_URL = "https://api.powerbi.com/beta/6295ca6a-f120-4460-8d95-acd0a015d672/datasets/c6e5342c-1e93-4282-aac9-89f0d2fa5363/rows?key=p4mdxodRF8H5ngZJmTbV%2FwolNqJMD2f4%2BRBnmEOsIFzgx8HFw2iQLKFd2MRbygZY7IHzw6LNKiSps%2Buofx0G%2FA%3D%3D"

# Gather temperature and sensor data and push to Power BI REST API

while True:
    try:
       # read and print out humidity and temperature from sensor

        temperature,pressure,humidity = bme280.readBME280All()

# ensure that timestamp string is formatted properly

        now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")

# data that we're sending to Power BI REST API

        data = '[{{ "timestamp": "{0}", "temperature": "{1:0.1f}", "pressure": "{2:0.1f}", "humidity": "{3:0.1f}" }}]'.format(now, temperature, pressure, humidity)

# make HTTP POST request to Power BI REST API

        req = urllib2.Request(REST_API_URL, data)

        response = urllib2.urlopen(req)

        print("POST request to Power BI with data:{0}".format(data))

        print("Response: HTTP {0} {1}n".format(response.getcode(), response.read()))



        time.sleep(60)

    except urllib2.HTTPError as e:

        print("HTTP Error: {0} - {1}".format(e.code, e.reason))

    except urllib2.URLError as e:

        print("URL Error: {0}".format(e.reason))

    except Exception as e:

        print("General Exception: {0}".format(e))
