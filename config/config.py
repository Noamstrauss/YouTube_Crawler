"""Configuration file"""

"""Steps:"""
#1. Install AWS CLI.
#2. Configure AWS CLI With A Admin frontend That Has Permissions To Create IAM Users & Create S3 OBjects.
#3. Insert Admin frontend Name Bellow.
#4. Create A Bucket In S3 And Insert The Name To bucket Config Bellow.
#5. Specify An Maximum frontend Age (max_user_age_seconds) in Config Bellow.
#6. Create An Policy Permission In IAM To Allow Users To View There Videos (see policy_example.txt).
#7. Specify Bellow Policy Permission ARN That You Created In Step 6.
#8. Run response.py.
#9. Run backend.py On backend.


#TODO Define Policy To set Users Permissions
permission = 'arn:aws:iam::352708296901:policy/S3VideoReader'


# TODO Define An Admin user Name That Will Not Be Deleted
admin = "aws35"


#TODO Define Bucket Name to upload Videos
bucket ='youtube-crawler-files'

#TODO Define frontend Maximun Subscriber age
max_user_age_seconds = (180.0)
#max_user_age_seconds = (172800.0)

#TODO Define Group To Add Users To (Group Is A Collection Of Policy's)
group = 'Youtube_Sub_Group'

#TODO If you are using a custom AWS_Profile enter it bellow
AWS_PROFILE = ""








