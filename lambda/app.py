import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(json.dumps({
        "message": "Lambda triggered",
        "event": event
    }))
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Mini Project 1!"})
    }
