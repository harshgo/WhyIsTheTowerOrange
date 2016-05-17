from getUpdate import getUpdate2
from postUpdate import postUpdate
from createPost import createPost

from time import sleep

#WEBSITE_URL = 'http://www.whyisthetowerorange.com'
WEBSITE_URL = "https://www.tower.utexas.edu/category/updates/"

NOT_ORANGE_OR_DARK = "Uuurgh. It's a sad day. No orange tower."

def main():

    while True:

        tower_action, reason = getUpdate2(WEBSITE_URL)

        update = createPost(tower_action, reason)

        if reason:

            postUpdate(update)

        else:

            postUpdate(NOT_ORANGE_OR_DARK)

        sleep(86400)

if __name__ == '__main__':
    main()
