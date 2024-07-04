# AML_Classification
This is an End to End Machine Learning project to predict the money laundering transactions.

Project Workflow
NOTE: Modular Coding Workflow
1. Update config.yaml
2. update params.yaml
3. Update the entity
4. Update the configuration manger in src config
5. Update the compontents
6. Update the pipeline
7. Update the main .py
8. Update the dvc.yaml # Update after completing all the pipeline needed for the project
Update secrets.yaml[optional]


Open EC2 and install docker in EC2 Machine

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker



SETUP GITHUB SECRETS

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app