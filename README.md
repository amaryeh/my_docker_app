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
- [start_app_pods.sh](./start_app_pods.sh): wrapper that calls the k8s yamls
- [app.py](app.py): the application code
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

## Test results
Testing scenario: 100 users sending 1 request per second over 9 minutes, with a ramp up and ramp down period.

TOTAL RESULTS

    checks_total.......................: 53607   104.524564/s
    checks_succeeded...................: 100.00% 53607 out of 53607
    checks_failed......................: 0.00%   0 out of 53607

    ✓ status was 200

    HTTP
    http_req_duration.......................................................: avg=6.19ms min=335.11µs med=2ms max=3.29s p(90)=3.25ms p(95)=4.16ms
      { expected_response:true }............................................: avg=6.19ms min=335.11µs med=2ms max=3.29s p(90)=3.25ms p(95)=4.16ms
    http_req_failed.........................................................: 0.00%  0 out of 53607
    http_reqs...............................................................: 53607  104.524564/s

    EXECUTION
    iteration_duration......................................................: avg=1s     min=1s       med=1s  max=4.29s p(90)=1s     p(95)=1s
    iterations..............................................................: 53607  104.524564/s
    vus.....................................................................: 1      min=0          max=100
    vus_max.................................................................: 100    min=100        max=100

    NETWORK
    data_received...........................................................: 8.4 MB 16 kB/s
    data_sent...............................................................: 7.1 MB 14 kB/s


