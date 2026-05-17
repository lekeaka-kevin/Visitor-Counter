# Visitor Counter API

A serverless visitor counter API built with Docker, AWS Lambda, DynamoDB, and deployed via CI/CD.

## Live API
[(https://hcnwdxp4h3tebjehbis6lkjosu0cehyl.lambda-url.eu-west-2.on.aws/)

## How it works
- Each GET request increments a counter in DynamoDB
- Returns the new count as JSON: `{"count": 42}`

## Architecture
- **Docker**: Containerized Python app
- **ECR**: Stores Docker images
- **Lambda**: Runs the container (serverless)
- **DynamoDB**: Stores visitor count
- **CodePipeline + CodeBuild**: CI/CD from GitHub
- **CloudFormation**: Infrastructure as Code

## Deployed with AWS CloudFormation
Two stacks:
- `visitor-counter-stack1`: ECR + DynamoDB + CodePipeline + CodeBuild
- `visitor-counter-stack2`: Lambda function using the container image

## Author
Kevin Lekeaka – AWS Certified Solutions Architect
