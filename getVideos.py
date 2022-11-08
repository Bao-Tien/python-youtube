import json
from youtubesearchpython import VideosSearch


def lambdaFunction(event, context):
    data = VideosSearch(event['searchKeyInput'], limit=10)

    return data.result()
