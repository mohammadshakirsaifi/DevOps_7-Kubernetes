# Flask Frontend & Express Backend on Kubernetes (Minikube)

This project demonstrates deploying a **Flask frontend** and an **Express backend** on a **local Kubernetes cluster using Minikube**.  
The Flask frontend communicates with the Express backend using Kubernetes Services.

---

## 📁 Project Structure

DevOps_7-Kubernetes/
├── README.md  
├── express-backend  
│   ├── Dockerfile  
│   ├── package.json  
│   └── server.js  
├── flask-frontend  
│   ├── Dockerfile  
│   ├── app.py  
│   ├── requirements.txt  
│   └── templates  
│       └── index.html  
├── k8s  
│   ├── express-deployment.yaml  
│   ├── express-service.yaml  
│   ├── flask-deployment.yaml  
│   └── flask-service.yaml  
└── screenshots  

---

## 🧩 Application Overview

| Component | Technology | Port |
|---------|-----------|------|
| Backend | Express (Node.js) | 3000 |
| Frontend | Flask (Python) | 5000 |

- Express backend exposes a REST endpoint.
- Flask frontend calls the backend using Kubernetes Service DNS.
- Applications are containerized using Docker and deployed on Minikube.

---

## 🔧 Prerequisites

- Docker
- Minikube
- kubectl
- Git

---

## ▶️ Deployment Steps

### 1️⃣ Start Minikube
```bash
minikube start
```
###### 📸 Screenshot: screenshots/1-Minikube-Start.png

2️⃣ Configure Docker to Use Minikube
eval $(minikube docker-env)

Verify:

docker info | grep Name

📸 Screenshot: screenshots/2-Docker-env.png

3️⃣ Build Docker Images
docker build -t express-backend ./express-backend
docker build -t flask-frontend ./flask-frontend

Verify:

docker images

📸 Screenshot: screenshots/3-Docker-Images.png

4️⃣ Deploy to Kubernetes
kubectl apply -f k8s/

📸 Screenshot: screenshots/4-kubectl-apply.png

5️⃣ Verify Pods and Services
kubectl get pods
kubectl get svc

📸 Screenshot: screenshots/5-pods-services.png

6️⃣ Verify Backend Output
kubectl port-forward svc/express-service 3000:3000

Open browser:

http://localhost:3000

📸 Screenshot: screenshots/6-Backend-Output.png

7️⃣ Access Flask Frontend
minikube service flask-service

📸 Screenshot: screenshots/7-Frontend-Browser.png

✅ Expected Output

Backend returns:

{ "message": "Hello from Express Backend!" }

Frontend displays the backend response in the browser.

