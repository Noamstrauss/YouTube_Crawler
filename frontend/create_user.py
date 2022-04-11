import boto3
from botocore.exceptions import ClientError
from termcolor import colored
import time
from config.config import *
from logger.user_logger import *

# AWS_PROFILE Config
custom_profile = bool(False)
if AWS_PROFILE != "":
    custom_profile = True
else:
    custom_profile = False

if custom_profile:
    session = boto3.session.Session(profile_name=AWS_PROFILE)

    client = session.client('iam')
else:
    client = boto3.client('iam')



# An Function That Creates An frontend In IAM
def create_user(username):

    try:
        response = client.create_user(
            UserName=username,
            PermissionsBoundary=permission,
            Tags=[
                {
                    'Key': 'YoutubeAppSubscriber',
                    'Value': username
                },
            ]
        )
        time.sleep(1.2)
        print("------------------------------------------------------------")
        log.info((colored("Successfully Created frontend '{}'".format(username), 'green')))
        print("------------------------------------------------------------")



    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            log.error(colored('user already exists', 'red'))
            log.info("Please Enter A Different frontend Name")
            username = input("Enter Username: ")

        else:
            log.error("Unexpected error: %s" % e)
            username = input("Enter Username: ")


if __name__ == '__main__':
    create_user("test2")