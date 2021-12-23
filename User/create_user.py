import boto3
from botocore.exceptions import ClientError
from termcolor import colored
import time
from config import *
client = boto3.client('iam')

# An Function That Creates An User In IAM
def create_user(username):

    while True:

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
            print((colored("Successfully Created User '{}'".format(username), 'green')))
            print("------------------------------------------------------------")

            break

        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(colored('User already exists', 'red'))
                print("Please Enter A Different User Name")
                username = input("Enter Username: ")
                continue
            else:
                print("Unexpected error: %s" % e)
                username = input("Enter Username: ")
                continue






if __name__ == '__main__':
    create_user("test")