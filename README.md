# Flask Frontend & Express Backend on Kubernetes (Minikube)

This project demonstrates deploying a **Flask frontend** and an **Express backend** on a **local Kubernetes cluster using Minikube**.  
The Flask frontend communicates with the Express backend using Kubernetes Services.

---

## 📁 Project Structure
 
<img width="392" height="663" alt="image" src="https://github.com/user-attachments/assets/aa8da963-2207-4fb6-a74e-802ba0667779" />

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

###  Start Minikube
```bash
minikube start
```
### 1. Minikube Start

![Minikube Start](screenshots/1-Minikube-Start.png)

---

### 2. Configure Docker to Use Minikube

```bash
eval $(minikube docker-env)
```

Verify:

```bash
docker info | grep Name
```

![Docker Environment](screenshots/2-Docker-env.png)

---

### 3. Build Docker Images

```bash
docker build -t express-backend ./express-backend
docker build -t flask-frontend ./flask-frontend
```

Verify:

```bash
docker images
```

![Docker Images](screenshots/3-Docker-Images.png)

---

### 4. Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

![Kubectl Apply](screenshots/4-kubectl-apply.png)

---

### 5. Verify Pods and Services

```bash
kubectl get pods
kubectl get svc
```

![Pods and Services](screenshots/5-pods-services.png)

---

### 6. Verify Backend Output

```bash
kubectl port-forward svc/express-service 3000:3000
```

Open browser:

```
http://localhost:3000
```

![Backend](screenshots/8-Backend.png)

![Backend Output](screenshots/9-Backend-Output.png)

---

### 7. Access Flask Frontend

```bash
minikube service flask-service
```

![Frontend](screenshots/6-Frontend.png)

![Frontend Browser](screenshots/7-Frontend-Browser.png)



