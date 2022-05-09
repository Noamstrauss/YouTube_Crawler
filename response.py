from frontend.create_user import create_user
from termcolor import colored
import time
import pyfiglet
from loguru import logger
from frontend.youtube import upload

def response(username,search_str,number=1):
    # App Welcome Sign
    welcome = pyfiglet.figlet_format("Youtube Crawler")
    print(welcome)

    # Welcome Message for newly subscribed user
    # print((colored("Welcome to Youtube Crawler By Noam -Ver. 1.1.0-beta ", 'blue', attrs=['bold'], )))
    # print("------------------------------------------------------------")
    time.sleep(1.2)
    logger.info('----------------------')
    logger.info('Start Log')
    # Creating a username for Youtube Crawler
    create_user(username)
    logger.info('User: {} Created!'.format(username))
    time.sleep(1.6)

    # Asking frontend for a Search String
    # If you only want to download a short test video enter ---> youtube-dl test video
    logger.info('User: {} selected {} to download'.format(username, search_str) )
    time.sleep(1.6)


    # Calling Youtube With search_str,search_results,username
    upload(username, search_str ,number)
    logger.info((colored("Uploaded Successfully {} ".format(search_str), 'green')))


if __name__ == '__main__':
    response("username","youtube-dl test video '/\ä↭𝕐")