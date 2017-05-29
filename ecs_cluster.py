from botocore.exceptions import ClientError
import boto3
import json
import re
from ecs import Ecs

class EcsCluster(Ecs):

    # initialize
    def __init__(self,ecs_json_file):
        super().__init__()
        self.ecs_json_file = ecs_json_file

        with open(self.ecs_json_file, 'r') as json_f:
            self.ecs_json     = json.load(json_f)
            self.clusterName  = self.ecs_json['clusterName']

    # check ecs cluster exists
    # return: True/False
    def is_exists(self):
        try:
            clustersr = self.ecs.list_clusters()

            for clusterArn in clustersr['clusterArns']:
                # clusterArn will be like...
                #     arn:aws:ecs:<Region>:<account>:cluster/<cluster name>
                name = re.sub('.*cluster\/','', clusterArn)

                if name == self.clusterName:
                    return True

                else:
                    continue

        except ClientError as err:
            return False
        
        else:
            return False

        finally:
            pass

    # create json file of specific ecs cluster.
    # file name as specific ecs cluster name.
    def get_cluster(self,name):
        try:
            response = self.ecs.describe_clusters(
                clusters=[name,],
            )

            f_name = "ecs-cluster-" + name + ".json"
            f = open(f_name, "w")
            cluster_json = response['clusters'][0]
            json.dump(cluster_json, f, indent=4, sort_keys=False)

        except ClientError as err:
            return False
        
        else:
            return True

        finally:
            pass

    # create ecs cluster
    def create(self):
        try:
            response = self.ecs.create_cluster(
                clusterName = self.clusterName
            )

            return response

        except ClientError as err:
            return err

