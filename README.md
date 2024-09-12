# k8s learning - Ingress

## Pre-requisites
* Having installed microk8s on wsl2 (https://microk8s.io/docs/install-wsl2)
* The ingress addon is enabled (https://microk8s.io/docs/addon-ingress)
* The registry addon is enabled (https://microk8s.io/docs/addon-registry)

## Installation
* Build the image
```sh
docker build -t hello-world-api:latest .
docker tag hello-world-api:latest localhost:32000/hello-world-api:latest
```

* Push the image to the registry
```sh
docker push localhost:32000/hello-world-api:latest
```

* Create the configmap
```sh
microk8s kubectl apply -f k8s.configmap.yaml

* Deploy the application
```sh
microk8s kubectl apply -f k8s.deployment.yaml
```

* Deploy the service
```sh
microk8s kubectl apply -f k8s.service.yaml
```

* Create the ingress rule
```sh
microk8s kubectl apply -f k8s.ingress.yaml
```

* Test the application
```sh
curl http://localhost/hello-world-api/hello | jq
```
