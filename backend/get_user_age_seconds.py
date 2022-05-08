import boto3
from datetime import datetime, timezone
from termcolor import colored
from config.config import *
from loguru import logger
client = boto3.client('iam')
# AWS_PROFILE Config
# custom_profile = bool(False)
# if AWS_PROFILE != "":
#     custom_profile = True
# else:
#     custom_profile = False
#
# if custom_profile:
#     session = boto3.session.Session(profile_name=AWS_PROFILE)
#
#     client = session.client('iam')
# else:
#     client = boto3.client('iam')

# A Function That Will Check Users Age to Send Age To delete_outdated_usernames Function
def get_user_age_seconds(username):

# Getting Users Dictionary From IAM

    response = client.get_user(
        UserName=username,
    )

# Striping Users Dictionary to get Create Date
    user_create_date = response['User']['CreateDate']


# Printing user Age To backend
#     if username != admin:
#         print("user ' {} ' is active (sec):".format(username),
#               (datetime.now(timezone.utc) - user_create_date).total_seconds())
#     else:
#         pass

# Calculating Users Age in Seconds
    user_seconds = (datetime.now(timezone.utc) - user_create_date).total_seconds()

# Determining if user Expired And Excluding Admin From Being Expired
    if user_seconds > max_user_age_seconds and username !=(admin):
        expired_sub = True

        logger.info((colored("user %s is expired " % username, 'red')))


    else:
        expired_sub = False

    return expired_sub

if __name__ == '__main__':
    get_user_age_seconds("test3")







