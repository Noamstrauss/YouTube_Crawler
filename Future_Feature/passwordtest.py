import boto3
from config import *
client = boto3.client('iam')
username=input("Enter UserName:")

#User Creation
response = client.create_user(
    UserName=username,
    PermissionsBoundary='arn:aws:iam::955114013936:policy/S3VideoReader',
    Tags=[
        {
            'Key': 'YoutubeAppSubscriber',
            'Value': username
        },
    ]


#Password Setup
)
password=input("Enter Password:")
response1 = client.create_login_profile(
    UserName=username,
    Password=password,
    PasswordResetRequired=False
)

#Group Add
response4 = client.add_user_to_group(
    GroupName=group,
    UserName=username
)
