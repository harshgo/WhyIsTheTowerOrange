import getUpdate
import postUpdate

from time import sleep

WEBSITE_URL = 'http://www.whyisthetowerorange.com'

def main():

    while True:

        reason = getUpdate.getUpdate(WEBSITE_URL)

        if reason:

            postUpdate.postUpdate(reason)

        sleep(86400)

if __name__ == '__main__':
    main()
