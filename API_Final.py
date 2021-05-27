

import hmac
import time
import requests
from base64 import urlsafe_b64encode
import json


# secret
key = "kizPmp6R1JXc43eoMvQAsyWGd8KU2bnjDrL5YFlE"

# 管理台获取accessKey、secretKey
accessKey = 'g5exMNZr07h1F2cmdGWVkInB9RU3HsT_6tEqLCJw'
secretKey = 'kizPmp6R1JXc43eoMvQAsyWGd8KU2bnjDrL5YFlE'

# APP或管理台获取设备识别码
deviceName = '7E5DBE24SMYH'


# token过期时间
expirationTime = int(time.time()) + 60 * 60

# class APIrequest():

def APIrequest(datakey, n):
    
    DATAKEY = datakey

    url = "https://storage.diandeng.tech/api/v1/ts?e={0}&device={1}&keyword={2}&quickDate=1h&queryType=avg".format(expirationTime, deviceName, DATAKEY)

    #获取token
    sign = urlsafe_b64encode(
        hmac.new(secretKey.encode("utf-8"),
                 url.encode("utf-8"), digestmod='sha1').digest()
    ).decode("utf-8")
    token = accessKey + ":" + sign
#     print(token)
    
    #获取URL
    URL = url + "&token="+token
#     print(URL)
    response = requests.get(URL)
    
#     print(URL)

## get length
    length = len(json.loads(response.text)['detail'])


    return json.loads(response.text)['detail'][length-1+n]['value']
 
# print(APIrequest('humisoil', 0))
  
    





