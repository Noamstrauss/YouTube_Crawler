import boto3
from youtube_dl import YoutubeDL
from termcolor import colored
from config.config import *
from loguru import logger


#ENV VARS
# YDL_OPTIONS = {'format': 'bestvideo', 'noplaylist':'True', 'extractaudio':'True', 'audioformat':'mp3'}
YDL_OPTIONS = {'noplaylist':'True',}
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
def search(search_str,number):
    try:
        YDL_OPTIONS['outtmpl'] = './static/{}.mp4'.format(search_str)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            videos = ydl.extract_info(f"ytsearch{number}:{search_str}", download=True)['entries']
            return [ydl.prepare_filename(video) for video in videos],
    except Exception as g:
        logger.error("Error", g)
        exit(1)

# S3 Upload Function
def upload(username,search_str,number=1):
    downloaded_files = search(search_str, number)
    try:
        for a in downloaded_files[0]:
            try:
                s3_client.upload_file(a, bucket,username + "/" + a)
                logger.info((colored("Downloaded Successfully {} ".format(a), 'green')))
            except Exception as g:
                logger.error("Error", g)
                exit(1)

    except Exception as e:
        logger.error("Error", e)
        exit(1)
