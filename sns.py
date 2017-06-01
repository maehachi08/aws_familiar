from botocore.exceptions import ClientError
import boto3
import json
from aws_familiar import AwsFamiliar

class Sns(AwsFamiliar):

    # initialize
    def __init__(self):
        self.sns = boto3.client('sns')

    # Sends a message to all of a topic's subscribed endpoints.
    #
    # resource = {
    #   "TopicArn": 'Topic ARN',
    #   "Message" : 'msg',
    #   "Subject" : 'subject'
    # }
    def publish(self,resource):
        self.sns.publish(
            TopicArn = resource['TopicArn'],
            Message  = resource['Message'],
            Subject  = resource['Subject']
        )


# sample
resource = {
    "TopicArn": 'arn:aws:sns:ap-northeast-1:XXXXXXXXXXXXXXX:XXXXXXXXXXXX',
    "Message" : 'msg',
    "Subject" : 'subject'
}

sns = Sns()
sns.publish(resource)

