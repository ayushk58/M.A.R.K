import requests
from pprint import pprint
import functions.Response

class Weather:
    def __init__(self):
        pass

    def weather_data(self,query):
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
        ret=res.json()
        return ret

    def weather_Response(self,result,city):
        res=str(result['main']['temp'])
        functions.Response.say("The current temparature is" + res)


def Weather_search(data):
    weather=Weather()
    city=data.split("for")
    query="q="+city[1]
    we_data=we_data(query)
    weather.weather_Response(we_data,city[1])
    



