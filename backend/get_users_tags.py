import boto3

client = boto3.client('iam')

response = client.list_users()
users_d = (response['Users'])
for user in users_d:
    tags = client.list_user_tags(UserName = user['UserName'])
    if tags['Tags']:
        for tag in tags['Tags']:
            if tag['Key'] == 'YoutubeAppSubscriber' and tag['Value'] == user['UserName']:
                print (user['UserName'])
else:
    print("No youtube sub's found!")
    exit(0)