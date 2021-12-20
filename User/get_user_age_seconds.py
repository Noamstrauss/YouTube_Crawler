import boto3
from datetime import datetime, timezone
from termcolor import colored
from config import *
client = boto3.client('iam')

# A Function That Will Check Users Age to Send Age To delete_outdated_usernames Function
def get_user_age_seconds(username):

# Getting Users Dictionary From IAM

    response = client.get_user(
        UserName=username,
    )

# Striping Users Dictionary to get Create Date
    user_create_date = response['User']['CreateDate']


# Printing User Age To Server
    if username != admin:
        print("User ' {} ' is active (sec):".format(username),
              (datetime.now(timezone.utc) - user_create_date).total_seconds())
    else:
        pass



# Calculating Users Age in Seconds
    user_seconds = (datetime.now(timezone.utc) - user_create_date).total_seconds()

# Determining if User Expired And Excluding Admin From Being Expired
    if user_seconds > max_user_age_seconds and username !=(admin):
        expired_sub = True

        print("User  ' {} ' is ".format(username),(colored('Expired', 'red')))
        print("--------------------------------------------")


    else:
        expired_sub = False

    return expired_sub

if __name__ == '__main__':
    get_user_age_seconds("noamsint")







