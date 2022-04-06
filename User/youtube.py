import boto3
from youtube_dl import YoutubeDL
from termcolor import colored
from config.config import *
from logger.user_logger import *

#ENV VARS
YDL_OPTIONS = {'format': 'bestvideo', 'noplaylist':'True'}
custom_profile = bool(False)
s3_client = boto3.client('s3')

#AWS_PROFILE CONFIG

# if AWS_PROFILE != "":
#     custom_profile = True
# else:
#     custom_profile = False
#
# if custom_profile:
#     session = boto3.session.Session(profile_name=AWS_PROFILE)
#     s3_client = session.client('s3')
# else:
#     s3_client = boto3.client('s3')


# Youtube-DL Serach Function
def search(arg,number):
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            videos = ydl.extract_info(f"ytsearch{number}:{arg}", download=True)['entries']
            return [ydl.prepare_filename(video) for video in videos],
    except Exception as g:
        log.error("Error", g)
        exit(1)

# S3 Upload Function
def upload(username,search_str,number=1):
    downloaded_files = search(search_str, number)
    try:
        for a in downloaded_files[0]:
            try:
                s3_client.upload_file(a, bucket,username + "/" + a)
                log.info((colored("Successfully Downloaded {} ".format(a), 'green')))
            except Exception as g:
                log.error("Error", g)
                exit(1)

    except Exception as e:
        log.error("Error", e)
        exit(1)
