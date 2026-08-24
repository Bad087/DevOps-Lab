\# Kubernetes Getting Started — Exercise 1



\## Business Problem



Imagine we are DevOps Engineers at Zepto. The product team has built

a lightweight web application for the storefront and delivery status

page.



For this exercise, the application is simulated using the Nginx

container image and deployed on a local Kubernetes cluster using

Minikube.



\## Objective



Deploy an Nginx application as a Kubernetes Pod, expose it using a

NodePort Service, and access it through a web browser.



\## Technologies Used



\- Kubernetes

\- Minikube

\- Docker

\- kubectl

\- Nginx



\## Environment



\- Operating System: Windows 11

\- Kubernetes: Minikube

\- Container Runtime: Docker

\- Kubernetes Version: v1.35.1

\- Minikube Version: v1.38.1

\- Docker Version: 29.4.1



\---



\## Step 1 — Start Minikube



The local Kubernetes cluster was started using:



```bash

minikube start --driver=docker

