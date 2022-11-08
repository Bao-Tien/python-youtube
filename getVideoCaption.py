import json
from youtubesearchpython import Transcript


def lambdaFunction(event, context):
    caption = Transcript.get(event['videoUrl'])
    return caption
