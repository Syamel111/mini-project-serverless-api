import json
import boto3
import os
import time

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE_NAME')
table = dynamodb.Table(table_name)

# ✅ Simple structured log helper
def log(message, level="INFO", **kwargs):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "level": level,
        "message": message,
        **kwargs
    }
    print(json.dumps(log_entry))

def lambda_handler(event, context):
    request_id = context.aws_request_id
    log("Lambda invoked", request_id=request_id, function="create_resume", status="started")

    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        email = body.get("email")
        resume_link = body.get("resume_link")

        if not name or not email or not resume_link:
            log("Missing required fields", level="ERROR", request_id=request_id, function="create_resume", status="error")
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing required fields"})
            }

        item = {
            "email": email,
            "name": name,
            "resume_link": resume_link
        }

        table.put_item(Item=item)

        log("Resume stored successfully", request_id=request_id, function="create_resume", status="success", email=email)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Resume stored successfully"})
        }

    except Exception as e:
        log("Unhandled exception", level="ERROR", error=str(e), request_id=request_id, function="create_resume", status="error")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
