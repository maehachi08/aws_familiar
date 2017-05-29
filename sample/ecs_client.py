from ecs_cluster import EcsCluster

file = "config/ecs.json"
ecs = EcsCluster(file)

if ecs.is_exists():
    print('ECS Cluster: ' + ecs.clusterName + ' found.')
else:
    print('ECS Cluster: ' + ecs.clusterName + ' not found.')

