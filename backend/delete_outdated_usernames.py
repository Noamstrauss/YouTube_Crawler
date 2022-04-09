import boto3
from botocore.exceptions import ClientError
from backend.get_user_age_seconds import get_user_age_seconds
from termcolor import colored
import time
from config.config import *
from logger.server_logger import *
client = boto3.client('iam')
s3 = boto3.resource('s3')
iam = boto3.resource('iam')
# #AWS_PROFILE CONFIG
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
#     s3 = session.resource('s3')
#     iam = session.resource('iam')
# else:
#     client = boto3.client('iam')
#     s3 = boto3.resource('s3')
#     iam = boto3.resource('iam')

policy = iam.Policy(permission)

log.info('----------------------')
log.info('Start Log')
# Deletes users older than max_user_age_seconds
def delete_outdated_usernames():

        try: # Delete
            response = client.list_users() # get all users in aws
            users_d = (response['Users']) # format list only to the user nested list ( dictionary)
            for x in range(len(users_d)):
                fo_user = users_d[x]['UserName']
                tags = client.list_user_tags(UserName=fo_user)
                if tags['Tags']:
                    for tag in tags['Tags']:
                        if tag['Key'] == 'YoutubeAppSubscriber' and tag['Value'] == fo_user:
                            expired = get_user_age_seconds(fo_user)
                            if expired == True and fo_user != admin:

                                # Trying To Delete Users Files From S3 Bucket After He Has Expired
                                try:
                                    # print((colored("Trying To Delete Users '{}' Files...".format(fo_user), 'yellow')))
                                    path = fo_user + "/"
                                    bucket1 = s3.Bucket(bucket)
                                    bucket1.objects.filter(Prefix=path).delete()
                                    # print((colored("Deleted Successfully '{}' Files".format(fo_user), 'green')))
                                    log.info((colored("Deleted %s Files Successfully" % fo_user, 'green')))
                                    # print("--------------------------------------------")
                                    time.sleep(2)
                                except ClientError as e:
                                    log.error("Unexpected error: %s" % e)
                                    time.sleep(2)

                                # Trying To Detach User From Policy
                                try:
                                    response_policy = policy.detach_user(
                                        UserName=fo_user)
                                    log.info((colored("Detached User %s Successfully" % fo_user, 'green')))
                                    time.sleep(2)

                                except client.exceptions.NoSuchEntityException :
                                    log.info((colored("User %s Policy Was Not Found" % fo_user, 'yellow')))
                                    time.sleep(2)

                                # Trying To Delete User Login Profile (Password)
                                try:
                                    response = client.delete_login_profile(
                                        UserName=fo_user)
                                    log.info((colored("Successfully Deleted  %s Login Profile" % fo_user, 'green')))
                                    time.sleep(2)

                                except client.exceptions.NoSuchEntityException:
                                    log.info((colored("Login Profile %s Not Found" % fo_user, 'yellow')))
                                    time.sleep(2)

                                # Trying To Remove User From Group (Permission)
                                try:
                                    response = client.remove_user_from_group(
                                        GroupName=group,
                                        UserName=fo_user)
                                    log.info((colored("Successfully Removed %s From Group" % fo_user, 'green')))
                                    time.sleep(2)

                                except client.exceptions.NoSuchEntityException:
                                    log.info((colored("Login Profile %s Not Found" % fo_user, 'yellow')))
                                    time.sleep(2)


                                """
                                try:
                                    print("Trying to Delete Access Key")
                                    response_del_acc = client.delete_access_key(
                                    AccessKeyId='AKIA54YJ3ITYDA3JMFOU',
                                    UserName=fo_user,)
                                    print(response_del_acc)
                                except ClientError as e:
                                    print("Unexpected error: %s" % e)
                                """
                                # Trying To Delete User From IAM
                                try:
                                    response_del = client.delete_user(
                                        UserName=fo_user)
                                    time.sleep(2)
                                    log.info((colored("Successfully Deleted User %s" % fo_user, 'green')))
                                    log.info("----------------------")
                                    time.sleep(2)
                                except ClientError as e:
                                    log.error("Unexpected error: %s" % e)
                                    time.sleep(2)
                                    pass
                                """
                                try:                     # iam output after Deletion
                                    if yes_or_no:  # If Statement Is True Printing Active Users In IAM
                                        response = client.list_users()
                                        for i in range(len(response['Users'])):
                                            if (response['Users'][i]['UserName']) == admin:
                                                print("Deleted All Exipred Users! - Only Admin User '{}' Is ACTIVE ".format(admin))
                                                time.sleep(3)
                                                log.info('----------------------')
                                                continue
                                            else:
                                                continue
                                    else:# iam output after Deletion else (If or no is FALSE)
                                        print("There Are No Sub's")
                                        log.info('No Subs')
                                        time.sleep(3.5)
                                        log.info('----------------------')
                                        log.info('End Log')
                                except:
                                    pass
                                """
                else:
                    time.sleep(1.5)
                    print('No Subs')
                    time.sleep(1.5)
                    print((colored("Only Admin User '%s' is active" % admin, 'yellow')))
                    time.sleep(1.5)


        except KeyboardInterrupt:
            log.info('End Log')
            log.info('----------------------')
            print((colored("Interrupted!", 'yellow')))
            exit(0)





