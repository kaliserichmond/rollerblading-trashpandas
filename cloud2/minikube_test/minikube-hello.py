from prefect import task, flow, get_run_logger
from prefect.filesystems import GitHub

github_block = GitHub.load("minikube-github-block")

@task
def hello():
    logger = get_run_logger()
    logger.info("Hello I'm a minikube flow.")

@flow
def myflow():
    hello_task = hello()
    print(hello_task)

if __name__ == "__main__":
    myflow()
