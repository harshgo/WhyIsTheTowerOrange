from bs4 import BeautifulSoup
import urllib2
import re


def getUpdate(url):

    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")

    div = soup.find("div", id="reason")
    children = div.findChildren()

    for child in children:

        if child.name == 'a':

            return unicode(child.string)
    return None

