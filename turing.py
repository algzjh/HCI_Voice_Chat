# -*- coding: utf-8 -*-
import requests
import json

KEY = 'c1b44fca97f44bbab61c4119d185836d'

def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": "长沙",
                    "province": "湖南",
                    "street": "麓山南路"
                }
            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": "Me"
        }
    }
    data = json.dumps(data)
    try:
        r = requests.post(apiUrl, data=data).json()
        return r['results'][0]['values']['text']
    except:
        return msg


if __name__ == '__main__':
    res = get_response("今天天气怎么样？")
    print(res)