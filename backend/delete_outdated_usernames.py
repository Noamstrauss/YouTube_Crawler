import boto3
from botocore.exceptions import ClientError
from backend.get_user_age_seconds import get_user_age_seconds
from termcolor import colored
import time
from config.config import *
from loguru import logger
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

logger.info('----------------------')
logger.info('Start Log')
# Deletes users older than max_user_age_seconds
def delete_outdated_usernames():
    response = client.list_users()  # get all users in aws
    users_d = (response['Users'])  # format list only to the user nested list ( dictionary)
    for x in range(len(users_d)):
        fo_user = users_d[x]['UserName']
        logger.info((colored("Checking if '{}' is a sub...".format(fo_user), 'magenta')))
        time.sleep(0.2)
        tags = client.list_user_tags(UserName=fo_user)
        if tags['Tags']:
            for tag in tags['Tags']:
                if tag['Key'] == 'YoutubeAppSubscriber' and tag['Value'] == fo_user:
                    # logger.info((colored("'{}' is a active sub!".format(fo_user), 'cyan')))
                    expired = get_user_age_seconds(fo_user)
                    if expired == True and fo_user != admin:

                        # Trying To Delete Users Files From S3 Bucket After He Has Expired
                        try:
                            # print((colored("Trying To Delete Users '{}' Files...".format(fo_user), 'yellow')))
                            path = fo_user + "/"
                            bucket1 = s3.Bucket(bucket)
                            bucket1.objects.filter(Prefix=path).delete()
                            # print((colored("Deleted Successfully '{}' Files".format(fo_user), 'green')))
                            logger.info((colored("Deleted {} Files Successfully".format(fo_user), 'green')))
                            # print("--------------------------------------------")
                            time.sleep(2)
                        except ClientError as e:
                            logger.error("Unexpected error: %s" % e)
                            time.sleep(2)

                        # Trying To Detach user From Policy
                        try:
                            response_policy = policy.detach_user(
                                UserName=fo_user)
                            logger.info((colored("Detached user {} Successfully".format(fo_user), 'green')))
                            time.sleep(2)

                        except client.exceptions.NoSuchEntityException:
                            logger.info((colored("user {} Policy Was Not Found".format(fo_user), 'yellow')))
                            time.sleep(2)

                        # Trying To Delete user Login Profile (Password)
                        try:
                            response = client.delete_login_profile(
                                UserName=fo_user)
                            logger.info((colored("Successfully Deleted {} Login Profile".format(fo_user), 'green')))
                            time.sleep(2)

                        except client.exceptions.NoSuchEntityException:
                            logger.info((colored("Login Profile {} Not Found".format(fo_user), 'yellow')))
                            time.sleep(2)

                        # Trying To Remove user From Group (Permission)
                        try:
                            response = client.remove_user_from_group(
                                GroupName=group,
                                UserName=fo_user)
                            logger.info((colored("Successfully Removed {} From Group".format(fo_user), 'green')))
                            time.sleep(2)

                        except client.exceptions.NoSuchEntityException:
                            logger.info((colored("Login Profile {} Not Found".format(fo_user), 'yellow')))
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
                        # Trying To Delete user From IAM
                        try:
                            response_del = client.delete_user(
                                UserName=fo_user)
                            time.sleep(2)
                            logger.info((colored("Successfully Deleted user {}".format(fo_user), 'green')))
                            logger.info("----------------------")
                            time.sleep(2)
                        except ClientError as e:
                            logger.error("Unexpected error: %s" % e)
                            time.sleep(2)
                            pass
                        """
                        try: # iam output after Deletion
                            if yes_or_no:  # If Statement Is True Printing Active Users In IAM
                                response = client.list_users()
                                for i in range(len(response['Users'])):
                                    if (response['Users'][i]['UserName']) == admin:
                                        print("Deleted All Exipred Users! - Only Admin user '{}' Is ACTIVE ".format(admin))
                                        time.sleep(3)
                                        logger.info('----------------------')
                                        continue
                                    else:
                                        continue
                            else:# iam output after Deletion else (If or no is FALSE)
                                print("There Are No Sub's")
                                logger.info('No Subs')
                                time.sleep(3.5)
                                logger.info('----------------------')
                                logger.info('End Log')
                        except:
                            pass
                        """
                    else:
                        logger.info((colored("User '{}' is active but not expired yet!".format(fo_user), 'yellow')))
    else:
        time.sleep(1.5)
        logger.info((colored("No Subs Found", 'green')))
        time.sleep(1.5)
        logger.info((colored("Only Admin user '{}' is active".format(admin), 'green')))
        time.sleep(1.5)
        # exit(0)

        # except KeyboardInterrupt:
        #     logger.info('End Log')
        #     logger.info('----------------------')
        #     print((colored("Interrupted!", 'yellow')))
        #     exit(1)
