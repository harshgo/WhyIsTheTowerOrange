from bs4 import BeautifulSoup
import urllib2
import re

CURRENT_POST_NUMBER_FILE_PATH = 'current_post_number.txt'

def getTitle(n, s):

    div = s.find("div", id=re.compile("post-[0-9]+"))
    current_post = int(div['id'].split('-')[1])

    title = None

    if current_post > n:

        children = div.findChildren()

        for child in children:

            if child.name == 'h2' and 'post-title' in child['class']:

                grandchildren = child.findChildren()

                for grandchild in grandchildren:

                    if grandchild.name == 'a':

                        title = unicode(grandchild.string)
                        break

    return (title, current_post)

def getUpdate(url):

    ''' DEPRECATED. DO NOT USE.'''

    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")

    div = soup.find("div", id="reason")
    children = div.findChildren()

    for child in children:

        if child.name == 'a':

            return unicode(child.string)

    return None

def getUpdate2(url):

    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website, 'html.parser')

    with open(CURRENT_POST_NUMBER_FILE_PATH) as f:
        n = int(f.readline())

    title, current_post_number = getTitle(n, soup)

    if title:

        with open(CURRENT_POST_NUMBER_FILE_PATH, 'w+') as f:
            f.write(str(current_post_number))

    return title
