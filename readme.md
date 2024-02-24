
### Prepare

* (optional) download lens dashboard https://k8slens.dev/
* download kubectl https://kubernetes.io/ru/docs/tasks/tools/install-kubectl/
* install helm https://helm.sh/docs/intro/install/

<hr>

### (optional) Minikube create cluster, push image
install minikube https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
```shell
# start cluster 
minikube start --kubernetes-version=v1.23.12 --memory 6144 --cpus 4 # --vm-driver=docker

# stop cluster
minikube stop

# (optional) dashboard
minikube dashboard

# load local image to minikube
minikube docker-env
# To point your shell to minikube's docker-daemon, run: 
# ........ execute it!

# build & push
cd airflow-build-image
docker build -t airflow_dwh:2.8.1 -f ./Dockerfile .
minikube image load airflow_dwh:2.8.1

# ls images
minikube image ls --format table
```

[//]: # (* create cluster in lens, name airflow)
[//]: # (* in terminal lens: `kubectl config view --minify --raw`, copy config in `~\.kube\config`)
[//]: # (* if your airflow image from local.docker.desktop, in settings Resources->WSL integration enable all checkbox)
[//]: # (kubectl create secret docker-registry regcred --docker-server=192.168.0.146:5555/dwh_group/airflow-build-local --docker-username=dwh --docker-password=dwhdwhdwh --docker-email=kek@lol)
[//]: # (# docker-compose -f docker-compose-postgres.yaml up -d)
[//]: # (## start dash)
[//]: # (## https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
[//]: # (#kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml)
[//]: # (## https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md)
[//]: # (#kubectl apply -f create-service-cccount.yaml)
[//]: # (#kubectl apply -f create-cluster-role-binding.yaml)
[//]: # (#kubectl -n kubernetes-dashboard create token admin-user)
[//]: # (#kubectl proxy)
[//]: # (## http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/)
[//]: # (# needed for pull local images)
[//]: # (kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson)
[//]: # (kubectl create secret generic regcred --from-file=.dockerconfigjson=C:\Users\Влад\.docker\config.json --type=kubernetes.io/dockerconfigjson)

<hr>

### (optional) Airflow KEDA (for worker autoscaling)
install keda https://airflow.apache.org/docs/helm-chart/stable/keda.html
```shell
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
kubectl create namespace keda
helm install keda kedacore/keda --namespace keda --version "v2.0.0"

# upgrade keda (if needed)
helm upgrade keda kedacore/keda --namespace keda --version "v2.0.0"
# uninstall keda
helm uninstall -n keda keda
```

<hr>

### Airflow
download helm https://github.com/apache/airflow/releases/tag/helm-chart%2F1.12.0
```shell
# start airflow cluster
kubectl create namespace airflow
helm install airflow -n airflow .

# proxy
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
kubectl port-forward svc/airflow-flower 5555:5555 --namespace airflow

# upgrade airflow
helm upgrade airflow -n airflow .
# uninstall airflow
helm uninstall airflow -n airflow
```

<hr>

### Output example:
```shell
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace airflow airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)
```

<hr>
