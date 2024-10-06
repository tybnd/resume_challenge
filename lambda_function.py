import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')  # Replace 'VisitorCount' with your table name

def lambda_handler(event, context):
    # Get the current visitor count from DynamoDB
    response = table.get_item(Key={'id': 'visitors'})
    visitor_count = response.get('Item', {}).get('count', 0)
    
    # Increment the count
    visitor_count += 1
    
    # Update the count in DynamoDB
    table.put_item(Item={'id': 'visitors', 'count': visitor_count})
    
    # Return the updated count
    return {
        'statusCode': 200,
        'body': json.dumps({'visitor_count': visitor_count}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

