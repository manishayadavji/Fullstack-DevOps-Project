# DevOps CI/CD Docker Project
  This project demonstrates automated deployment of a containerized web application using Jenkins and Docker on AWS EC2.


## Project Structure
project-folder
│
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── index.html
│   └── style.css
│
├── docker-compose.yml


## Tech Stack
- Docker
- Docker Compose
- Jenkins
- AWS EC2
- Python Flask
- GitHub

## CI/CD Pipeline
1. Code pushed to GitHub
2. Jenkins pulls the latest code
3. Docker Compose builds containers
4. Application deployed on EC2

## Application
Frontend: http://EC2_PUBLIC_IP:3000  
Backend API: http://EC2_PUBLIC_IP:5000/api/status
