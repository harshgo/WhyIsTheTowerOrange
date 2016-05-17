from getUpdate import getUpdate2
from postUpdate import postUpdate
from createPost import createPost

from time import sleep

#WEBSITE_URL = 'http://www.whyisthetowerorange.com'
WEBSITE_URL = "https://www.tower.utexas.edu/category/updates/"

NOT_ORANGE_OR_DARK = "Uuurgh. It's a sad day. No orange tower."

def main():

    while True:

        tower_action, reason = getUpdate2(WEBSITE_URL) # Is the tower dark or orange? If so, why? Both are None if today is a sad day.

        update = createPost(tower_action, reason) # Create a sentence (update) from the towers' status and the reason.

        if reason:

            postUpdate(update) # Post the update to Twitter

        else:

            postUpdate(NOT_ORANGE_OR_DARK) # The tower is just busy towering. Today is a sad day.

        sleep(86400) # Wait for 24 hours. Urgh.

if __name__ == '__main__':
    main()
