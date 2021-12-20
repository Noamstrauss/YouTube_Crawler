from User.create_user import create_user
from termcolor import colored
from User.yes_or_no import yes_or_no
from User.number_input import number_vali
import time
import pyfiglet
from User.loggetsetup import *


# App Welcome Sign
welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

# Welcome Message for newly subscribed user
print((colored("Welcome to Youtube Crawler By Noam -Ver. 1.1.0-beta ", 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")
time.sleep(1.2)
play = True
while play:
    try:
        # Asking for Username and Creating a User
        username = input("Please Enter A Username: ")

        # Creating a username for Youtube Crawler
        create_user(username)
        logger.info('User: %s Created!',username)

        # Greeting The New User
        time.sleep(1.2)
        print((colored("Hey there {} lets Start Having Fun!\U0001f60d ".format(username), 'cyan', )))
        print("------------------------------------------------------------")
        time.sleep(1.2)

        # Asking User for a Search String
        # If you only want to download a short test video enter ---> youtube-dl test video
        search_str = input("Please Enter A Topic To Download: ")
        print("------------------------------------------------------------")
        time.sleep(1.2)

        # Asking User For A Number Of Videos To Download
        number = number_vali("Please Enter A Number Of Videos To Download: ")
        print("------------------------------------------------------------")
        time.sleep(1.2)

        # Importing Youtube Downloader And Uploader To AWS S3 Bucket
        from User.youtube_crawler import upload
        

        # Calling Youtube With search_str,search_results,username
        upload(username, search_str, number)

        logger.info('Downloded Successfully %s ',search_str)

        # Asking User If To Create Another User
        print("------------------------------------------------------------")
        play = yes_or_no("Do You Want To Create Another User?")
        if play == True:
            play = True
            continue
        else:
            play = False
            pass



    except KeyboardInterrupt:
        print('Interrupted!')



# Printing A User A Thank You Note
print("------------------------------------------------------------")
print((colored('Thank You for Using Youtube Crawler By Noam \U0001f60d', 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")
print("See You Next Time \U0001f600")
print("------------------------------------------------------------")
logger.info('----------------------')
logger.info('End Log')
exit(0)












