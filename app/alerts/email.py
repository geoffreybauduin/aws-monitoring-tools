import boto3
from config import config

def send_email(section, key, value):
    client = boto3.client("ses",
                          aws_access_key_id=config.get(section, "aws_access_key"),
                          aws_secret_access_key=config.get(section, "aws_secret_key"),
                          region_name=config.get(section, "aws_region"))
    response = client.send_email(
        Source=config.get("email", "from"),
        Destination={
            'ToAddresses': [config.get(section, "email_to")],
            'CcAddresses': [],
            'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': 'SQS queue {} key {} value {} not changing'.format(section, key, value),
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': 'SQS queue {} key {} value {} not changing'.format(section, key, value),
                    'Charset': 'utf-8',
                },
                'Html': {
                    'Data': 'SQS queue {} key {} value {} not changing'.format(section, key, value),
                    'Charset': 'utf-8',
                }
            }
        },
    )