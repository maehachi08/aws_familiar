import unittest
import json
from ecs_cluster import EcsCluster

file = "tests/config/ecs.json"
class EcsClusterTest(unittest.TestCase):

    def test_is_exists(self):
        ecs = EcsCluster(file)
        self.assertTrue( ecs.is_exists() )

    def test_create(self):
        with open(file, 'r') as json_f:
            ecs_json    = json.load(json_f)
            clusterName = ecs_json['clusterName']

        ecs = EcsCluster(file)
        response = ecs.create()

        self.assertTrue( response['cluster']['clusterName'] == clusterName )


if __name__ == "__main__":
    unittest.main()

