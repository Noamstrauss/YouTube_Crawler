import boto3

iam_client = boto3.client('iam')

response = iam_client.list_users()
for user in response['Users']:
    tags = iam_client.list_user_tags(UserName = user['UserName'])
    if tags['Tags']:
        for tag in tags['Tags']:
            if tag['Key'] == 'YoutubeAppSubscriber' and tag['Value'] == user['UserName']:
                print (user['UserName'])