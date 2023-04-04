Bosch-Final-Project

CI/CD with Azure Cloud for a Kubernetes-Based Web Application
This project aims to build a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Kubernetes-based web application using Azure Cloud and Kubernetes. The Azure Kubernetes Service (AKS) will be used for container orchestration.

CI/CD Pipeline

The pipeline is triggered by a new commit to the dev branch
The pipeline includes several stages, including running a monitoring script, performing a SonarQube analysis, exporting GitHub Actions metrics, building and pushing a Docker image, and deploying to Azure Kubernetes Service
Each stage has its own job, and some jobs depend on the success of other jobs
The pipeline ensures that the application is thoroughly tested and analyzed for quality before being deployed to production

Metrics and Monitoring

The monitoring script collects metrics for CPU usage, RAM usage, and disk space usage
The SonarQube analysis collects metrics related to code quality, such as code smells and security vulnerabilities
The GitHub Actions exporter collects metrics related to the GitHub repository, such as the duration of workflow runs and the status of runner machines
Prometheus is used to store and display the collected metrics
The monitoring tool provides valuable insights into the performance and quality of the application

Deployment

The deployment process is automated through the pipeline, which uses infrastructure as code to ensure consistency and repeatability
The application is deployed to both a production and a staging environment, which allows for testing and validation before releasing to users
The deployment process is simplified through the use of Azure Kubernetes Service, which provides scalable and reliable container orchestration

Infrastructure as Code

The infrastructure is defined as code using Azure CLI, which allows for version control and reproducibility
Infrastructure as code ensures that the environment is consistent and repeatable, which is important for managing and scaling the application
Infrastructure as code also enables faster and more efficient deployment, since the infrastructure can be provisioned automatically


Project Components

Python Rest API with FastAPI
Azure Kubernetes Service (AKS)
Automation Server
GitHub Actions
SonarQube
Prometheus
Grafana
Project Setup
Install Azure CLI.
Create a Kubernetes cluster in AKS.
Install FastAPI for the Python Rest API.
Configure SonarQube for static analysis.
Install Prometheus and Grafana for monitoring.
Use GitHub Actions for automation.
Create the CI/CD pipeline to build, validate, and deploy the web application to the AKS cluster.
Create the cloud configuration as code.

Conclusion

This project demonstrates the power of using Azure Cloud and Kubernetes for deploying a web application. The CI/CD pipeline ensures software quality in production and automates the deployment process, saving time and resources. With the help of monitoring tools like Prometheus and Grafana, developers can easily visualize metrics and gain insights into the performance of their applications.
