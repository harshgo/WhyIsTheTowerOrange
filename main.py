from getUpdate import getUpdate2
from postUpdate import postUpdate

from time import sleep

#WEBSITE_URL = 'http://www.whyisthetowerorange.com'
WEBSITE_URL = "https://www.tower.utexas.edu/category/updates/"

def main():

    while True:

        reason = getUpdate2(WEBSITE_URL)

        if reason:

            postUpdate(reason)

        sleep(86400)

if __name__ == '__main__':
    main()
