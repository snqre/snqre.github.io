'''
'''
import requests, json


class Exchange():
    def __init__():
        pass

    def get_price(name :str):
        location :str ='https://api.coingecko.com/api/v3/simple/price?ids='+str(name)+'&vs_currencies=usd'
        request =requests.get(location)
        json_content =request._content
        content =json.loads(json_content)
        return content #return python dict

    def json_save(var :dict):
        ''' return python class =dictionary in Json '''
        json_content =json.dumps(var, indent =1, sort_keys =False)
        return json_content

    def update():
        pass