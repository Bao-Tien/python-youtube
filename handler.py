import json
from youtubesearchpython import VideosSearch


def dayLaTenHam(event, context):
    # body = {
    #     "message": "Go Serverless v3.0! Your function executed successfully!",
    #     "input": event,
    # }

    # response = {"statusCode": 200, "body": json.dumps(body)}

    data = VideosSearch('Hieu Nguyen', limit = 10)

    return data.result()

