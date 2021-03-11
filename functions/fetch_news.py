import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import functions.Response
import assistant

class News():
    def __init__(self):
        pass
    def get_headlines(self):
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        news_link=[]
        for news in news_list[:11]:
            news_link.append(news)
            new=str(news.title.text)
            functions.Response.say(new)
            
            

        functions.Response.say("Would you like to read any of them sir?Please specify")
        link=functions.Response.listen()
        try:
            if(assistant.word2num(link)):
                num=assistant.word2num(link)
                urlopen(news_link[num])
            else:
                functions.Response.say("I guess i could not understand ")
        except:
            functions.Response.say("Okay Sir")


def News_search():
    news=News()
    news.get_headlines()