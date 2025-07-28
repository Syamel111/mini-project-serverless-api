import json
import boto3
import os
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME'])

# Structured logger
def log(message, level="INFO", **kwargs):
    print(json.dumps({
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "level": level,
        "message": message,
        **kwargs
    }))

def lambda_handler(event, context):
    request_id = context.aws_request_id
    log("Lambda invoked", level="INFO", function="create_resume", request_id=request_id)

    try:
        if event["requestContext"]["http"]["method"] != "POST":
            log("Method not allowed", level="ERROR", request_id=request_id)
            return {
                "statusCode": 405,
                "body": json.dumps({"message": "Method Not Allowed"})
            }

        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        email = body.get("email")
        resume_link = body.get("resume_link")

        if not name or not email or not resume_link:
            log("Missing required fields", level="ERROR", request_id=request_id)
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing required fields"})
            }

        table.put_item(Item={
            "email": email,
            "name": name,
            "resume_link": resume_link
        })

        log("Resume stored successfully", level="INFO", request_id=request_id, email=email)
        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Resume stored successfully"})
        }

    except Exception as e:
        log("Unhandled exception", level="ERROR", request_id=request_id, error=str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
