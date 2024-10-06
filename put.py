import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

def put_item(visitor_id, count):
    try:
        # Update the item in DynamoDB
        response = table.update_item(
            Key={
                'ID': visitor_id
            },
            UpdateExpression='SET VisitorCount = :val',
            ExpressionAttributeValues={
                ':val': count
            },
            ReturnValues='UPDATED_NEW'
        )
        return response
    except ClientError as e:
        print(f"Error updating item: {e.response['Error']['Message']}")
        return None

def lambda_handler(event, context):
    if event.get('httpMethod') == 'POST' and event.get('path') == '/put':
        body = json.loads(event.get('body', '{}'))
        visitor_id = body.get('visitor_id', 'default_id')
        count = body.get('count', 0)
        response = put_item(visitor_id, count)
        status_code = 200
        message = 'Item updated successfully' if response else 'Failed to update item'
    else:
        status_code = 404
        message = 'Not Found'

    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Allow CORS if needed
        },
        'body': json.dumps({
            'message': message
        })
    }
