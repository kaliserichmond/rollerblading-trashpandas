# Tutorials


## Discourse / Linen 
- https://discourse.prefect.io/tag/aws
- What are the three most recent questions users have asked about aws or ecs or eks
- When would you choose EC2 vs EKS vs ECS? Which do you recommend and why?

## Execution Environments & Infra
where the flow will run and where the agent lives.
- EC2 - docker or subprocess
- EKS - kubernetes job
- ECS - docker or ecstask

## Storage (Flow code)
- S3
- Github
- Docker Container

## Results 
- S3

## Things to try
- Put the kubernetes agent on EKS and run your flow
- Spin up the agent on ECS and run a flow
- Configure results to S3 

## Resources 
- https://medium.com/the-prefect-blog/prefect-2-4-0-release-adds-support-for-aws-ecs-and-improves-deployment-cli-for-ci-cd-9582458e1e81
- https://github.com/PrefectHQ/prefect-recipes/tree/main/devops/infrastructure-as-code/aws/cli-prefect2-ecs-agent
- https://towardsdatascience.com/prefect-aws-ecs-fargate-github-actions-make-serverless-dataflows-as-easy-as-py-f6025335effc#8d94
- https://docs.prefect.io/concepts/infrastructure/#ecstask

## Bonus
- create a lambda function that executes a flow without an agent 
- create a lambda function that triggers a flowrun with the client api
