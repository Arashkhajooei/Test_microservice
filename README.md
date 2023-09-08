# Microservices Architecture README

This repository contains a set of microservices built with FastAPI in Python that communicate with each other. These microservices are designed to run in Docker containers and can be deployed to various environments, including your local machine and cloud platforms like Azure.


## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Local Development](#local-development)
  - [Deployment to Azure Container Instances](#deployment-to-azure-container-instances)
- [Usage](#usage)
- [Testing](#testing)
- [Monitoring and Scaling](#monitoring-and-scaling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This microservices architecture consists of three services:

1. **Service1**:
   - Accepts integer input via a POST request.
   - Communicates with Service2 to calculate the square of the input.
   - Communicates with Service3 to print the result.
   
2. **Service2**:
   - Receives requests from Service1 to calculate the square of an input.
   - Validates the input and calculates the square.
   - Communicates with Service3 to print the result.

3. **Service3**:
   - Receives requests from Service2 to print the result.
   - Prints the result and returns it.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your local machine.
- Azure CLI (if deploying to Azure Container Instances).
- Azure Container Registry (ACR) set up with your Docker images (if deploying to Azure).

## Getting Started

### Local Development

To run the microservices locally for development and testing:

1. Clone this repository:

   ```shell
   git clone <repository_url>
   cd <repository_directory>

2. Build the Docker images for each service:
   
   ```shell
   docker build -t service1-image -f service1/Dockerfile .
   docker build -t service2-image -f service2/Dockerfile .
   docker build -t service3-image -f service3/Dockerfile .

3. Create a custom Docker network:

   ```shell
   docker network create my-network

4. Run the containers for each service, ensuring they are on the same network:

   ```shell
   docker run -d --name service1-container -p 8001:8001 --network my-network service1-image
   docker run -d --name service2-container -p 8002:8002 --network my-network service2-image
   docker run -d --name service3-container -p 8003:8003 --network my-network service3-image

## Deployment to Azure Container Instances
If you want to deploy the microservices to Azure Container Instances (ACI):
1. Push your Docker images to Azure Container Registry (ACR):
   ```shell
   # Authenticate to your ACR
    az acr login --name <your_acr_name>
    
    # Push the images
    docker push <your_acr_name>.azurecr.io/service1-image
    docker push <your_acr_name>.azurecr.io/service2-image
    docker push <your_acr_name>.azurecr.io/service3-image

3. Use the Azure CLI or Azure Portal to create ACIs for each service, specifying the image and networking settings.
4. Access the public IP addresses of the ACIs to test the microservices.

## Testing
You can run tests for each microservice individually using test frameworks like Pytest. Detailed testing instructions can be found in the respective service directories.
## Monitoring and Scaling
Monitor the performance and logs of your microservices using Azure monitoring tools. You can also implement scaling strategies within Azure Container Instances to handle increased traffic.
## Usage
To use the microservices, you can send POST requests to the respective endpoints of Service1, and the microservices will communicate with each other to perform the requested operations.
Here's an example using **'curl'** to test Service1:
   ```shell
   curl -X POST -d '{"value": 5}' -H "Content-Type: application/json" http://localhost:8001/input

