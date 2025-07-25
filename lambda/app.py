import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Lambda triggered")
    
    # Simulate an error to trigger CloudWatch Alarm
    logger.error("Simulated failure for alert test")

    return {
        "statusCode": 200,
        "body": '{"message": "Testing error alert"}'
    }
