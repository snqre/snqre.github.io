# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# GET DATA FROM COINGEKO
import requests, json

class Exchange:
    def __init__(self):
        #get initial data from database
        self.db :dict ={
            'ethereum' :0.00935,
            'locgame' :309779.77
        }

    def update(self, asset :str, balance :float):
        self.db.update(asset, balance)

def get_price(name :str):
        location :str ='https://api.coingecko.com/api/v3/simple/price?ids='+str(name)+'&vs_currencies=usd'
        request =requests.get(location)
        json_content =request._content
        content =json.loads(json_content)
        return content[name]['usd'] #return python dict

def json_save(var :dict):
        ''' return python class =dictionary in Json '''
        json_content =json.dumps(var, indent =1, sort_keys =False)
        return json_content


# --------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# import
from flask import Flask, redirect, url_for, render_template


# init
app =Flask(__name__)
app.config['SECRET_KEY'] ='9f49c910cadd9162cdfd5a4dee9d5f0e795f0c9281873123b35f961031399dc8'

def get_growth_symbol(x):
    if x >0:
        return '+'
    else:
        return ''

percentage_change = 8.91
# page :: home
@app.route('/')
def index():
    caption:str='Vault.'

    navbar_option_0:str=''
    navbar_option_1:str=''
    growth:str=str(get_growth_symbol(percentage_change))+str(percentage_change)
    background_color_0='#EE7752'
    background_color_1='#E73C7E'
    background_color_2='#23A6D5'
    background_color_3='#23D5AB'
    timeframe:str='24H'
    return render_template(
        'index.html',
        growth=growth,
        caption=caption,
        timeframe=timeframe,
        navbar_option_0=navbar_option_0,
        navbar_option_1=navbar_option_1,
        current_share_price =round(((0.00935 *get_price('ethereum')) +(309779.77 *get_price('locgame'))) /1543677.47, 5),
        background_color_0=background_color_0,
        background_color_1=background_color_1,
        background_color_2=background_color_2,
        background_color_3=background_color_3
    )

print('Successful')
#run
if __name__ =='__main__':
    app.run(debug=True)
