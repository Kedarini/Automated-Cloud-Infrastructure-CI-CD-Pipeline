# Automated Cloud Infrastructure CI/CD Pipeline

A cloud-native, containerized task management application with an automated CI/CD pipeline. It combines a FastAPI backend, a simple frontend, Kubernetes manifests (Kustomize), and GitHub Actions to demonstrate container orchestration, declarative deployments and pipeline automation.

## Tech Stack

| Layer | Technology |
| :-- | :-- |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **Containerization** | [Docker](https://www.docker.com/) |
| **Orchestration** | [Kubernetes](https://kubernetes.io/) |
| **Configuration** | [Kustomize](https://kustomize.io/) |
| **CI/CD** | [GitHub Actions](https://github.com/features/actions) |
| **Version Control** | [Git](https://git-scm.com/) |

## Architecture

```text
[GitHub Actions (CI/CD)] → [Docker Build & Push] → [Kubernetes Manifests (Kustomize)]
                                                        ↓
                                                    [K8s Cluster]
                                                    ├─ Tasks API (FastAPI)
                                                    ├─ Frontend
                                                    └─ PostgreSQL/DB (via manifests)
    
    
The project focuses on a declarative, reproducible deployment approach using Kubernetes manifests, with automation handled through GitHub Actions.
    
Features
- Containerized microservices – Backend (tasks-api) and frontend run in isolated containers.
- Kubernetes-native – Includes Deployment, Service and configuration manifests for local (kind/minikube) or remote clusters.
- Kustomize-based configuration – Uses kustomization.yaml to manage environment-specific overrides in a declarative way.
- CI/CD ready – GitHub Actions workflows handle build and validation to ensure consistency across changes.
- Cloud-native design – Separation of concerns between application code, containers and deployment manifests.
    
Project Structure
.
├── .github/workflows/   # CI/CD workflows
├── frontend/            # Static frontend
├── tasks-api/           # FastAPI backend
├── k8s/                 # Kubernetes manifests
├── kustomization.yaml   # Kustomize configuration
└── README.md
    
Getting Started
    
Prerequisites
- Docker
- kubectl
- Kustomize (or built-in kubectl kustomize)
- A local Kubernetes cluster (e.g. kind, minikube)
    
Deploy to Kubernetes (Local)
1. Clone the repository
git clone https://github.com/Kedarini/Automated-Cloud-Infrastructure-CI-CD-Pipeline.git
cd Automated-Cloud-Infrastructure-CI-CD-Pipeline
2. Build and push images (optional if using local cluster with kind load/minikube image load)
docker build -t tasks-api:latest ./tasks-api
docker build -t frontend:latest ./frontend
3. Apply manifests with Kustomize
kubectl apply -k .
4. Verify the deployment
kubectl get pods
kubectl get svc
    
CI/CD
    
GitHub Actions workflows are located in .github/workflows/. They focus on validating the build process and maintaining consistency of the containerized workloads on each push/PR.
    
Project Goals.
    
The goal of this project was to gain hands-on experience with Kubernetes manifests, Kustomize, container orchestration, and CI/CD automation by deploying a small, working application in a cloud-native way.
