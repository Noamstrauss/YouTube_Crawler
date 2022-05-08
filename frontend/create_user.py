import boto3
from botocore.exceptions import ClientError
from termcolor import colored
import time
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
        logger.info((colored("Successfully Created User '{}'".format(username), 'green')))
        print("------------------------------------------------------------")



    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            logger.error((colored("Username '{}' already exists".format(username), 'red')))
            logger.info("Please Enter A Different User Name")


        else:
            logger.error("Unexpected error: %s" % e)



# if __name__ == '__main__':
#     create_user("test3")