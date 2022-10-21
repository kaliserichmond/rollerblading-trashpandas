from prefect import task, Flow
from prefect.tasks.prefect import create_flow_run


def extract_some_data():
    # return "some-random-piece-of-data"
    return {"param_key": [],
            "foo": []}

with Flow("parent-flow") as flow:
    data = extract_some_data()

    # assumes you have registered a flow named "example" in a project named "examples"
    flow_run = create_flow_run(flow_name="kalise-example",
                               project_name="test",
                               parameters=data)


flow.register(project_name="test")