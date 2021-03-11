import wikipedia
import functions.Response
import webbrowser
import inflect
import assistant
from googlesearch import search
import time

webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                
class Wikipedia:
    def __init__(self):
        pass
    def wiki_search(self,data):
        result=wikipedia.summary(data,sentences=2)
        functions.Response.say(result)

class Google:
    def __init__(self):
        pass
    def Google_Search(self,data):
        url="https://google.com/search?q="+data
        webbrowser.open(url)
    def Open_page(self,data,query):
        links=[]
        for url in search(query,tld='com', lang='en', num=5, start=0, stop=4, pause=2.0):
            links.append(url)
        functions.Response.say("Opening the specified link sir")
        webbrowser.open(links[data-1])
        time.sleep(1)
        functions.Response.say("link opened Sir")

def Search(data):
    if "wikipedia" in data:
        wiki=Wikipedia()
        query=data.split("for")
        wiki.wiki_search(query[1])
    elif "google" in data:
        google=Google()
        query=data.split("for")
        google.Google_Search(query[1])
        time.sleep(1)
        functions.Response.say("Which link would you want me to open Sir??Please specify")
        command=functions.Response.listen()
        try:
            if(assistant.word2num(command)):
                num=assistant.word2num(command)
                google.Open_page(num,query[1])
            else:
                functions.Response.say("Sorry Sir, But I recommend searching in top 5 links, other than that there is no useful information on other site")
        except:
            functions.Response.say("Okay Sir")
        

        

