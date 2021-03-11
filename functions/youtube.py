import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import webbrowser
import functions.Response

class Youtube:
    def __init__(self):
        pass
    def play_music(self,data):
        music_name =str(data)
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        print(clip2)
        webbrowser.open(clip2)

def Play_music(data):
    play=Youtube()
    data=data.split("play")
    functions.Response.say("PLaying the" + str(data[1]) + "On youtube")
    play.play_music(data[1])
