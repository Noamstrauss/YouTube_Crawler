"""Configuration file"""

"""Steps:"""
#1. Install AWS CLI.
#2. Create An Bucket In S3 And Insert The Name To bucket Config Bellow.
#3. Configure AWS CLI With A Admin User That Has Permissions To Create IAM Users & Create S3 OBjects.
#4. Insert Admin User Name Bellow.
#5. Specify An Maximum User Age (max_user_age_seconds) in Config Bellow.
#6. Create An Policy Permission In AWS IAM To Allow Users To View There Videos.
#7. Specify  Bellow Policy Permission ARN That You Created In Step 6.
#8. Run User/USER_INTERFACE.py.
#9. Run Server/SERVER.py On Server.


#TODO Define Policy To set Users Permissions
permission = 'arn:aws:iam::955114013936:policy/S3VideoReader'

# TODO Define An Admin User That Will Not Be Deleted
admin = "noamsint"


#TODO Define Bucket Name to upload Videos
bucket ='youtube-crawler-bucket'

#TODO Define User Maximun Subscriber age
max_user_age_seconds = (2.0)
#max_user_age_seconds = (172800.0)

#TODO Define Group To Add Users To (Group Is A Collection Of Policy's)
group = 'Youtube_Sub_Group'







