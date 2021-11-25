import boto3
from youtube_dl import YoutubeDL
from termcolor import colored
s3_client = boto3.client('s3')
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}


def search(arg,number):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        videos = ydl.extract_info(f"ytsearch{number}:{arg}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos],



def upload(username,search_str,number):
    downloaded_files = search(search_str, number)
    try:
        for a in downloaded_files[0]:
            try:
                s3_client.upload_file(a, 'youtube-crawler-bucket',username + "/" + a)
                print((colored("Successfully Downloaded {} ".format(a), 'green')))
            except Exception as g:
                print("Error", g)
                exit(1)

    except Exception as e:
        print("Error", e)
        exit(1)