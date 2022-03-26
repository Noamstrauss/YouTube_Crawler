import boto3
from botocore.exceptions import ClientError
from Server.get_user_age_seconds import get_user_age_seconds
from termcolor import colored
import time
from config.config import *
from logger.server_logger import *

#AWS_PROFILE CONFIG
custom_profile = bool(False)
if AWS_PROFILE != "":
    custom_profile = True
else:
    custom_profile = False

if custom_profile:
    session = boto3.session.Session(profile_name=AWS_PROFILE)

    client = session.client('iam')
    s3 = session.resource('s3')
    iam = session.resource('iam')
else:
    client = boto3.client('iam')
    s3 = boto3.resource('s3')
    iam = boto3.resource('iam')

policy = iam.Policy(permission)



# Deletes users older than max_user_age_seconds
def delete_outdated_usernames():

    # Asking If To Print Of List Of Users After Deletion
    #yes_or_no("Would You Like To View Status of Sub's After Deletion?")

    while True:
        try: # Delete
            response = client.list_users()
            users_d = (response['Users'])
            for x in range(len(users_d)):
                fo_user = users_d[x]['UserName']
                log.info('Start Log')
                expired = get_user_age_seconds(fo_user)
                if expired == True and fo_user != admin:

                    # Trying To Delete Users Files From S3 Bucket After He Expired
                    try:
                        # print((colored("Trying To Delete Users '{}' Files...".format(fo_user), 'yellow')))
                        path = fo_user + "/"
                        bucket1 = s3.Bucket(bucket)
                        bucket1.objects.filter(Prefix=path).delete()
                        # print((colored("Deleted Successfully '{}' Files".format(fo_user), 'green')))
                        log.info('Deleted %s Files Successfully' % fo_user)
                        # print("--------------------------------------------")
                        time.sleep(2)
                    except ClientError as e:
                        # print("Unexpected error: %s" % e)
                        log.error("Unexpected error: %s" % e)
                        time.sleep(2)

                    # Trying To Detach User From Policy
                    try:
                        # print((colored("Trying To Detach User '{} ' From Policy...".format(fo_user), 'yellow')))
                        response_policy = policy.detach_user(
                            UserName=fo_user)
                        log.info('Detached User %s Successfully' % fo_user)
                        # print((colored("Successfully Detached '{}' From Policy".format(fo_user), 'green')))
                        # print("--------------------------------------------")
                        time.sleep(2)

                    except client.exceptions.NoSuchEntityException :
                        # print('User %s Policy Was Not Found' % fo_user)
                        log.info('User %s Policy Was Not Found' % fo_user)
                        # print("--------------------------------------------")
                        time.sleep(2)

                    # Trying To Delete User Login Profile (Password)
                    try:
                        # print((colored("Trying To Delete '{}''s Login Profile ...".format(fo_user),
                        #                'yellow')))
                        response = client.delete_login_profile(
                            UserName=fo_user)
                        log.info('Successfully Deleted  %s Login Profile' % fo_user)
                        # print((colored("Successfully Deleted '{}' Login Profile".format(fo_user), 'green')))
                        # print("--------------------------------------------")
                        time.sleep(2)

                    except client.exceptions.NoSuchEntityException:
                        # print('Login Profile Not Found')
                        log.info('Login Profile  Not Found')
                        # print("--------------------------------------------")
                        time.sleep(2)

                    # Trying To Remove User From Group (Permission)
                    try:
                        # print((colored("Trying To Remove '{}' From Group ...".format(fo_user),
                        #                'yellow')))
                        response = client.remove_user_from_group(
                            GroupName=group,
                            UserName=fo_user)
                        log.info('Successfully Removed  %s From Group' % fo_user)
                        # print((colored("Successfully Removed '{}' From Group".format(fo_user), 'green')))
                        # print("--------------------------------------------")
                        time.sleep(2)

                    except client.exceptions.NoSuchEntityException:
                        # print('Login Profile %s Not Found' % fo_user)
                        log.info('Login Profile %s Not Found' % fo_user)
                        # print("--------------------------------------------")
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
                        # print((colored("Trying To Delete User '{}'...".format(fo_user), 'yellow')))
                        response_del = client.delete_user(
                            UserName=fo_user)
                        time.sleep(2)
                        # print((colored("Successfully Deleted '{}'".format(fo_user), 'green', attrs=['bold'],)))
                        log.info('Successfully Deleted User %s' % fo_user)
                        # print("--------------------------------------------",)
                        # print("\n")
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
                    # print("There Are No Sub's")
                    time.sleep(1.5)
                    log.info('No Subs')
                    time.sleep(1.5)
                    # print("There Are No Sub's")
                    print("Only Admin User '{}' Is ACTIVE ".format(admin))
                    time.sleep(1.5)
                    log.info('End Log')
                    log.info('----------------------')
                    time.sleep(1.5)


        except KeyboardInterrupt:
            print('Interrupted!')
            exit(0)





