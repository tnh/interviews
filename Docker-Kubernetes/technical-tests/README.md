# Solution Description

## Docker file Fix
Fixed Dockerfile has been updated and pushed to this repo

## Multistage DockerBuild
A multi-stage build has been used where a "baseimage" is used from the build cache and the modified app will only be copied into the intermediate image 

## Kubernetes Deployment
A helm chart has been created under 'goapp/' and 

```bash
helm install . --generate-name  
```
Running the above command from the ```goapp/``` directory should get you the following output. Helm will be using your existing kubernetes context, in this case i used docker-desktop

``` bash
NAME: chart-1632060921
LAST DEPLOYED: Mon Sep 20 00:15:22 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=goapp,app.kubernetes.io/instance=chart-1632060921" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

the ```values.yaml``` has the configuration parameters and they have been commented, the chart logic neednt be changed for CD

a set of sample manifests have been generated and pushed under './sample_template.yml', helm will template the manifests upon deployment, this is just a sample


## CI using github actions
github actions have been used for CI and the 'latest' image is being pushed into a private dockerhub repo 
