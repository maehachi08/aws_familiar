from botocore.exceptions import ClientError
import boto3
import json
from aws_familiar import AwsFamiliar

class Ecs(AwsFamiliar):

    # initialize
    def __init__(self):
        self.ecs = boto3.client('ecs')

