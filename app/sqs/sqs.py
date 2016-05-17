import boto3
from config import config
from app.check_methods import check

def check_queue(section):
    client = boto3.client("sqs",
                          aws_access_key_id=config.get(section, "aws_access_key"),
                          aws_secret_access_key=config.get(section, "aws_secret_key"),
                          region_name=config.get(section, "aws_region"))
    response = client.get_queue_attributes(
        QueueUrl=config.get(section, "queue"),
        AttributeNames=[
            'ApproximateNumberOfMessages',
        ]
    )
    check_method = config.get(section, "check_method")
    check(check_method, section, section, response['Attributes']['ApproximateNumberOfMessages'])
    return int(response['Attributes']['ApproximateNumberOfMessages'])