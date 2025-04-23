# my_docker_app
A K8S cluster on minikube, with a simple service that exposes an API to end users.
## Requirements:
- Input: Product ID
- Output: Corresponding Price for that product
- Handles a high number of users
- No authentication

## Implementation
- Using Python with Flask and WSGI.
- Scaling with HPA.
- Testing with K6.

### Details
### Prerequisites
1. Docker desktop
2. minikube, including metrics server 
'minikube addons enable metrics-server'
3. kubectl
4. k6-operator 
'git clone https://github.com/grafana/k6-operator && cd k6-operator'

