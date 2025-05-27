# Realtime Lead Scoring System
Dataset used: https://www.microsoft.com/en-us/research/project/mslr/
## Trainin methodology

The model has been trained using XGBoost XGBRanker on AWS Sagemaker

This has been trained using a custom Dockerfile placed in the root of this repository
The resulting model is stored in s3 and has been downloaded into the inferenceapi folder

## Deployment Strategy
Case 1:

If the inference is required in a more time-delayed fashion i.e. it is not required instantaneously. Then processing it in a pipeline with probably a Lambda function works well. The results would then get stored in a database, to be retrieved later for the business

Case 2:

If the inference required is relatively instantaneous, we should consider using a REST API based operation. They can be of the following options:

1. Lambda function exposed over API Gateway
2. Fastapi/Flask API service running in a container on EKS or AWS Fargate

## Design for REST API 

The model in question should be stored in some kind of model registry or at the bare minimum, s3

For a production-grade API, the healthcheck should work only when the model has been loaded in memory. A event trigger should be included at the start of the application where the model is being loaded into memory. Depending on the use-case, download time of the model from the registry should also be considered.

[FASTAPI Code](inferenceapi/)

Lambda functions should be avoided in case of large files being downloaded and the inference being run only in certain timeframes but needs low latency. This is due to the cold start problem in Lambda functions where is is not initalized when it has not been used for a long time.

Also in cases where we need to scale up. Which Lambda functions do automatically, the new instances will face the same issue of cold start.

Containerized deployments work really well in such scenarios where depending on the incoming traffic, we can always have a minimum of 1 container/pod running at any point in time, While the requests get queued up and can be then be sent to the newly spun up pods/instances which have been set to autoscale

## Infrastructure setup

The details of the Infrastructure setup has been mentioned in [Infrastructure](/Infrastructure.md)

## CI/CD setup

The details of the CI/CD setup has been mentioned in [CI/CD](/CICD.md)