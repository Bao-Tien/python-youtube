import json
from youtubesearchpython import *
fetcher = StreamURLFetcher()


def lambdaFunction(event, context):
    videoInfo = Video.getInfo(event['videoId'], mode=ResultMode.json)
    return videoInfo
