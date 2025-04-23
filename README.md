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
`minikube addons enable metrics-server`
3. kubectl
4. k6-operator `git clone https://github.com/grafana/k6-operator && cd k6-operator`

### Files
- start_app_pods.sh: wrapper that calls the k8s yamls
- app.py: the application code
- prices.txt: flatfile mapping product id to price. Downloaded on pod instantiation, so can be updated.
- dockerfile: used to build the image.
- requirements.txt: python prereqs used by docker when building the image.
- deployment.yaml: runs the image with the app
- service.yaml: creates a loadbalancer service in front of the pods
- hpa.yaml: Horizontal pod autoscaler. Scales number of pods up and down in response to load, as seen through the metrics.
- pod.yaml: a pod with bash for manual tests.
- bundle.yaml: k6 pods infra yaml.
- test.js: test code for k6. Added with `kubectl create configmap k6-test --from-file=test.js`
- testrun.yaml: k6 test pods.