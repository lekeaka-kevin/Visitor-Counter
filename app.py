import json
import boto3
from datetime import datetime
from decimal import Decimal

# Helper function to convert Decimal to int/float for JSON
def decimal_to_int(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    try:
        # Get current count
        response = table.get_item(Key={'id': 'visitor_count'})
        
        if 'Item' in response:
            # Convert Decimal to int
            current_count = int(response['Item']['count'])
        else:
            current_count = 0
        
        # Increment
        new_count = current_count + 1
        
        # Save to DynamoDB
        table.put_item(
            Item={
                'id': 'visitor_count',
                'count': new_count,
                'last_updated': datetime.utcnow().isoformat()
            }
        )
        
        # Return success - use default=str to handle Decimal
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
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
