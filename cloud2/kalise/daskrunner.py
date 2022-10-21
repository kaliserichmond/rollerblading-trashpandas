from prefect import flow, task, allow_failure
from prefect_dask.task_runners import DaskTaskRunner
import time

def sim_failure(task_name: str):
    if task_name == "task_2":
        raise Exception("Failure")

@task()
def sql_task(task_name: str):
    print(f"Running task: {task_name}")
    sim_failure(task_name)
    time.sleep(3)

@flow(name="demo_4",task_runner=DaskTaskRunner())
def demo_4():
    task_1 = sql_task.with_options(name="task_1").submit(task_name="task_1", wait_for=[])
    task_2 = sql_task.with_options(name="task_2").submit(task_name="task_2", wait_for=[allow_failure(task_1)])
    task_3 = sql_task.with_options(name="task_3").submit(task_name="task_3", wait_for=[allow_failure(task_2)])

if __name__ == "__main__":
    demo_4()

# prefect deployment build workflows/old_tests/demo_4.py:demo_4 -n test-basic -q test-queue
# prefect deployment apply demo_4-deployment.yaml
# python workflows/old_tests/demo_4.py