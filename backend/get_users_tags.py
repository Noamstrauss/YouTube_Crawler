import boto3
from termcolor import colored
from loguru import logger
client = boto3.client('iam')
active = False
response = client.list_users()
users_d = (response['Users'])
for x in range(len(users_d)):
    fo_user = users_d[x]['UserName']
    logger.info((colored("Checking if '{}' is a sub...".format(fo_user), 'magenta')))
    tags = client.list_user_tags(UserName=fo_user)
    if tags['Tags']:
        for tag in tags['Tags']:
            if tag['Key'] == 'YoutubeAppSubscriber' and tag['Value'] == fo_user:
                logger.info((colored("'{}' is a active sub!".format(fo_user), 'green')))
                active = True
else:
    if not active:
        logger.info((colored("No youtube sub's found!", 'red')))
    exit(0)
