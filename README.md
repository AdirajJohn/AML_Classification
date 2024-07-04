# AML_Classification

**Project Description:**
* This end-to-end project aims to identify money laundering transactions by leveraging the power of data science and software engineering methodologies.
* Developed a classification model using Random Forest and implemented modular coding practices for organized development and easier maintenance.
* Implemented MLOps concepts using MLflow for experiment tracking and DVC for pipeline tracking, ensuring reproducibility and efficient resource management.
* Utilized AWS S3 Bucket for Data Ingestion Pipeline to pull the data from the cloud using Python's boto3 package.
* Developed a Flask-based front-end interface for convenient machine learning model access, achieving a 91% accuracy rate in predicting money laundering transactions.
* Deployed the model using AWS EC2 and ECR services and implemented a CI/CD pipeline using Git Actions to automate the stages of software development.

**Modular Coding Workflow:**
1. Update `config.yaml`
2. Update `params.yaml`
3. Update the entity
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `the main.py` file
8. Update `dvc.yaml` (Update after completing all the pipelines needed for the project)
9. Update `secrets.yaml` (optional)

The above steps ensure an organized and systematic approach to developing and maintaining the AML_Classification project.

**Future Development:**

1. Implement pipeline orchestration using Apache Airflow for scheduling pipeline tasks to run at specific times and monitoring pipeline performance.
2. Implement the MLOps concepts of model drift and data drift.
3. Utilize DVC for data versioning.
4. Handle missing values in prediction data in production.
5. Implement A/B testing to compare different model versions.
6. Integrate SHAP and LIME tools for enhanced explainability of the model.
7. Monitor performance using Prometheus, Grafana, or the ELK Stack (Elasticsearch, Logstash, Kibana) for logging and monitoring.


SETUP
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