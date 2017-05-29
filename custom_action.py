#!/usr/bin/env python3.5
# -*- conding: utf-8 -*-

from botocore.exceptions import ClientError
import boto3
import json
from codepipeline import Codepipeline

class CustomAction(Codepipeline):

    # initialize
    def __init__(self,custom_action_define_file):
        super().__init__()
        self.action_file   = custom_action_define_file

        with open(self.action_file, 'r') as json_f:
            self.custom_action_json = json.load(json_f)
            self.category = self.custom_action_json['category']
            self.provider = self.custom_action_json['provider']
            self.version  = self.custom_action_json['version']
            self.settings = self.custom_action_json['settings']
            self.configurationProperties = self.custom_action_json['configurationProperties']
            self.inputArtifactDetails    = self.custom_action_json['inputArtifactDetails']
            self.outputArtifactDetails   = self.custom_action_json['outputArtifactDetails']

    # check custom action exists
    # return: True/False
    def is_exists(self):
        try:
            response = self.codepipeline.list_action_types(
                actionOwnerFilter = 'Custom'
            )

            for action in response['actionTypes']:
                if action['id']['category'] == self.category and \
                   action['id']['provider'] == self.provider and \
                   action['id']['version']  == self.version:
                    return True

                else:
                    continue

        except ClientError as err:
            return False
        
        else:
            return False

        finally:
            pass

    # create custom action
    def create(self):
        response = self.codepipeline.create_custom_action_type(
            category = self.category,
            provider = self.provider,
            version  = self.version,
            settings = self.settings,
            configurationProperties = self.configurationProperties,
            inputArtifactDetails    = self.inputArtifactDetails,
            outputArtifactDetails   = self.outputArtifactDetails
        )

