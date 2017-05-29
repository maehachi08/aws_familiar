#!/usr/bin/env python3.5
# -*- conding: utf-8 -*-

'''
    Description:
        AWS Codepipeline management

    Sample Usage:
        file   = 'pipeline.json'
        object = Codepipeline(file)
        if object.is_exists():
            print('CodePipeline: ' + object.pipeline_name + ' found.')
        else:
            print('CodePipeline: ' + object.pipeline_name + ' not found.')
        
            try:
                object.create()
            except ClientError as err:
                print('CodePipeline: ' + object.pipeline_name + ' create failed.')
            else:
                print('CodePipeline: ' + object.pipeline_name + ' created.')
            finally:
                pass

'''

from botocore.exceptions import ClientError
import boto3
import json
from codepipeline import Codepipeline

class Pipeline(Codepipeline):

    # initialize
    def __init__(self,pipeline_file):
        super().__init__()
        self.pipeline_file = pipeline_file

        with open(self.pipeline_file, 'r') as json_f:
            self.codepipeline_json = json.load(json_f)
            self.pipeline_name = self.codepipeline_json['pipeline']['name']

    # check pipeline exists
    # return: True/False
    def is_exists(self):
        try:
            response = self.codepipeline.get_pipeline(
                name = self.pipeline_name
            )
        
        except ClientError as err:
            return False
        
        else:
            return True

        finally:
            pass

    # create json file of specific pipeline.
    # file name as specific pipeline name.
    def get_pipeline(self):
        try:
            response = self.codepipeline.get_pipeline(
                name = self.pipeline_name
            )

            f = open(self.pipeline_name + ".json", "w")
            pipeline_json = { "pipeline" : response['pipeline'] }
            json.dump(pipeline_json, f, indent=4, sort_keys=False)

        except ClientError as err:
            return False
        
        else:
            return True

        finally:
            pass

    # create pipeline
    def create(self):
        response = self.codepipeline.create_pipeline(
            pipeline={
                'name'          : self.pipeline_name,
                'roleArn'       : self.codepipeline_json['pipeline']['roleArn'],
                'artifactStore' : self.codepipeline_json['pipeline']['artifactStore'],
                'stages'        : self.codepipeline_json['pipeline']['stages'],
                'version'       : self.codepipeline_json['pipeline']['version']
            }
        )

    # update pipeline
    def update(self):
        response = self.codepipeline.update_pipeline(
            pipeline={
                'name'          : self.pipeline_name,
                'roleArn'       : self.codepipeline_json['pipeline']['roleArn'],
                'artifactStore' : self.codepipeline_json['pipeline']['artifactStore'],
                'stages'        : self.codepipeline_json['pipeline']['stages'],
                'version'       : self.codepipeline_json['pipeline']['version']
            }
        )



