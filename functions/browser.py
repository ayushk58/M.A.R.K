import webbrowser
import functions.Response

class Browser:
    def __init__(self):
        pass
    def open_browser(self,url):
        webbrowser.open(url)


def Open_Browser(data):
    data=data.split(" ")
    page=data[-1]
    browser=Browser()
    url="https://"+page+".com"
    functions.Response.say("Opening "+page+".com please give me a sec")
    browser.open_browser(url)


