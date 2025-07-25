import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Lambda triggered")


    return {
        "statusCode": 200,
        "body": '{"message": "Hello from Mini Project 1"}'
    }
