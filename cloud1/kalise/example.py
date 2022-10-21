from prefect import task, Flow, Parameter

@task
def extract_some_data(input):
    for x in input:
        print(x)
    return "some-random-piece-of-data"

with Flow("kalise-example") as flow:
    input = Parameter("param_key", default=[])
    input2 = Parameter("foo", default=[])
    data = extract_some_data(input)

flow.register(project_name="test")