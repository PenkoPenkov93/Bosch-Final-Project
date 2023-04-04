# Bosch-Final-Project

CI/CD with Azure Cloud for a Kubernetes-Based Web Application
This project aims to build a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Kubernetes-based web application using Azure Cloud and Kubernetes. The Azure Kubernetes Service (AKS) will be used for container orchestration.

The pipeline will include jobs that ensure software quality in production. One such job will execute a static analysis for every new commit available in the repository. Initially, this job should trigger a build for every new commit.

The build job should include a checkout step and a script to build the project. For static analysis, SonarQube will be used.

The metrics from SonarQube analysis will be uploaded to Prometheus through the SonarQube-Prometheus exporter plugin. The GitHub action metrics exported from the GitHub repository will also be available in Prometheus.

During the pipeline's execution, a program will be used to calculate the amount of process time, RAM memory, and physical disk space used. These metrics will be visualized through a monitoring tool.

The deployment will happen in two environments: Production and Staging. The cloud configuration will be stored as code and should be easily replicated for a new setup. The infrastructure as code is handled with Azure CLI.

The pipeline will automate the build, validation, and deployment of the web application to an Azure Kubernetes cluster.

Project Components
The following components will be used for this project:

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
