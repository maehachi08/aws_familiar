#!/usr/bin/env python3.5
# -*- conding: utf-8 -*-

from botocore.exceptions import ClientError
import boto3
import json
from aws_familiar import AwsFamiliar

class Codepipeline(AwsFamiliar):

    # initialize
    def __init__(self):
        self.codepipeline = boto3.client('codepipeline')

