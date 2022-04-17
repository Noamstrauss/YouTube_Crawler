from frontend.create_user import create_user
from termcolor import colored
from validation.yes_or_no import yes_or_no
from validation.number_input import number_vali
import time
import pyfiglet
from logger.user_logger import *
from frontend.youtube import upload

def response(username,search_str,number=1):
    # App Welcome Sign
    welcome = pyfiglet.figlet_format("Youtube Crawler")
    print(welcome)

    # Welcome Message for newly subscribed user
    # print((colored("Welcome to Youtube Crawler By Noam -Ver. 1.1.0-beta ", 'blue', attrs=['bold'], )))
    # print("------------------------------------------------------------")
    time.sleep(1.2)
    log.info('----------------------')
    log.info('Start Log')
    # Creating a username for Youtube Crawler
    create_user(username)
    log.info('User: %s Created!', username)
    time.sleep(1.6)

    # Asking frontend for a Search String
    # If you only want to download a short test video enter ---> youtube-dl test video
    log.info('User: %s selected %s to download', username, search_str)
    time.sleep(1.6)


    # Calling Youtube With search_str,search_results,username
    upload(username, search_str ,number)
    log.info((colored("Uploaded Successfully {} ".format(search_str), 'green')))


if __name__ == '__main__':
    response("username","youtube-dl test video '/\ä↭𝕐")