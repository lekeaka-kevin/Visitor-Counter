import json
import boto3
from datetime import datetime

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    """
    This function runs every time the API is called.
    It increments the visitor counter and returns the new count.
    """
    try:
        # Try to get the current count from DynamoDB
        response = table.get_item(Key={'id': 'visitor_count'})
        
        # If the item exists, use its count. Otherwise start at 0.
        if 'Item' in response:
            current_count = response['Item']['count']
        else:
            current_count = 0
        
        # Increment the count
        new_count = current_count + 1
        
        # Save the new count back to DynamoDB
        table.put_item(
            Item={
                'id': 'visitor_count',
                'count': new_count,
                'last_updated': datetime.utcnow().isoformat()
            }
        )
        
        # Return the count as JSON
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'count': new_count,
                'message': 'Visitor counter incremented successfully'
            })
        }
    
    except Exception as e:
        # If anything goes wrong, log the error and return a 500
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Internal server error'
            })
        }
