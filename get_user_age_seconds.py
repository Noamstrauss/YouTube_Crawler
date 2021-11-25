import boto3
from datetime import datetime, timezone
from termcolor import colored
import time
client = boto3.client('iam')

# Defining An Admin User That Will Not Be Deleted
admin = "noamsint"

# A Function That Will Check Users Age to Send Age To delete_outdated_usernames Function
def get_user_age_seconds(username):

# Getting Users Dictionary From IAM

    response = client.get_user(
        UserName=username,
    )

# Striping Users Dictionary to get Create Date
    user_create_date = response['User']['CreateDate']


# Printing User Age To Server
    if username == admin:
        print("The Are No Subscribers Yet")
        time.sleep(5)
    else:
        print("User ' {} ' is active (sec):".format(username),(datetime.now(timezone.utc) - user_create_date).total_seconds())

# Defining Maximum Subscriber Age in Seconds
    #max_user_age_seconds = (172800.0)
    max_user_age_seconds = (2.0)

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







