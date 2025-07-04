import boto3
import os

sns = boto3.client('sns')
s3 = boto3.client('s3')

SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    # Get bucket and object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Get the file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode('utf-8')
    
    # Count words
    word_count = len(text.split())
    
    # Format message
    subject = 'Word Count Result'
    message = f'The word count in the {key} file is {word_count}.'
    
    # Send notification
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )
    
    return {
        'statusCode': 200,
        'body': message
    }
