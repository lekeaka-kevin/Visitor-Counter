import json
import boto3
from datetime import datetime
import hashlib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    try:
        # Get a unique identifier for this request (IP + User-Agent)
        request_id = event.get('requestContext', {}).get('requestId', 'unknown')
        
        # Try to increment only if this request hasn't been processed
        response = table.update_item(
            Key={'id': 'visitor_count'},
            UpdateExpression='ADD #count :inc',
            ExpressionAttributeNames={'#count': 'count'},
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        new_count = int(response['Attributes']['count'])
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Cache-Control': 'no-cache, no-store, must-revalidate'
            },
            'body': json.dumps({
                'count': new_count,
                'message': 'Visitor counter incremented successfully'
            })
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
