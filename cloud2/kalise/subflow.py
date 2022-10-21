from prefect import task, flow

@flow()
def second_subflow(list):
    for x in list:
        print(x)

@flow()
def subflow(name):
    print(name)
    list = []
    return list

@flow()
def parent_flow():
    list = subflow('Kalise')
    somethingelse = []
    second_subflow(somethingelse)

parent_flow()