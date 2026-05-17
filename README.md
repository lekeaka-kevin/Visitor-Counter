# Visitor Counter API

A serverless visitor counter that increments and returns a count each time the API is called. The application is containerized with Docker, deployed to AWS Lambda, and automated with a CI/CD pipeline.

## Live API
[(https://hcnwdxp4h3tebjehbis6lkjosu0cehyl.lambda-url.eu-west-2.on.aws/)

## Architecture
- **Docker + ECR**: Python app containerized and stored in Elastic Container Registry
- **Lambda**: Runs the container on demand (serverless, scales to zero)
- **DynamoDB**: Stores the visitor count (serverless NoSQL)
- **CodePipeline + CodeBuild**: CI/CD pipeline triggered by GitHub pushes
- **CloudFormation**: Infrastructure as Code (two stacks)

## How It Works
1. You make a GET request to the Lambda Function URL
2. Lambda invokes the containerized Python app
3. The app reads the current count from DynamoDB
4. Count increments
5. New count is saved back to DynamoDB
6. JSON response returns the updated count

## Cost
All services used are within AWS Free Tier limits:
- Lambda: 1M requests/month
- DynamoDB: 25GB storage
- ECR: 500MB storage
- CodeBuild: 100 build minutes/month
- CodePipeline: 1 pipeline free

**Monthly cost for personal use: $0**

## GitHub
[(https://github.com/lekeaka-kevin/Visitor-Counter)
## Author
Kevin Lekeaka
