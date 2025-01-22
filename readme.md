# Heart-Disease-Detection MLops

## Description

This project implements a Machine Learning Operations (MLops) pipeline to automate the deployment of a heart disease detection application. The key features include:

1. **CI/CD Pipeline**:

   - **CI (Continuous Integration)**: A GitHub Actions pipeline that runs on every push to the repository. It executes scripts for data ingestion, processing, model training, and evaluation. Following these steps, a Docker image is built and pushed to Docker Hub.
   - **CD (Continuous Deployment)**: Once the CI pipeline completes, the CD pipeline is triggered. It connects to an AWS EC2 instance, pulls the latest Docker image, removes any running containers, and deploys the new container.

2. **Data Pipeline**:

   - Data ingestion, processing, and model training scripts are modularized in the `src` folder. These scripts ensure that the latest data is used to train and evaluate the model, making it production-ready.

3. **AWS Deployment**:
   - The application is hosted on an AWS EC2 instance. Docker ensures seamless containerization, enabling easy updates and scalability. \href{http://3.110.165.70:8501/}{Deployed Link}

---

## Project Flow

![Project Flowchart](https://github.com/Dharansh-Neema/heart-disease-ml-project/blob/main/img/FlowChart.png)

---

## Setup Instructions

To run the application locally using Docker, follow these steps:

1. Pull the Docker image from Docker Hub:

   ```bash
   docker pull dharanshneema/heart-disease-detection-ml
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8051:8051 dharanshneema/heart-disease-detection-ml
   ```

3. Access the application:
   Open your browser and navigate to:
   [http://localhost:8051](http://localhost:8051)

The application should now be running locally on your system.
