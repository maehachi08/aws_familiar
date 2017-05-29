from pipeline import Pipeline

file   = "config/pipeline.json"
pipeline = Pipeline(file)

if pipeline.is_exists():
    print('CodePipeline: ' + pipeline.pipeline_name + ' found.')

else:
    print('CodePipeline: ' + pipeline.pipeline_name + ' not found.')

    try:
        pipeline.create()

    except ClientError as err:
        print('CodePipeline: ' + pipeline.pipeline_name + ' create failed.')

    else:
        print('CodePipeline: ' + pipeline.pipeline_name + ' created.')

    finally:
        pass

