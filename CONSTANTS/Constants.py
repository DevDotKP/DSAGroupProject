import requests

HEADER = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest"
}

PRODUCTION = 'Production'


def readhtml(url) :
    r = requests.get ( url=url, headers=HEADER )
    return r
