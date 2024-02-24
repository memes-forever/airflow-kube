## build
`docker build . -f Dockerfile -t airflow_dwh:2.8.1`

## login in local registry
`docker login 192.168.0.146:5555/dwh_group/airflow-build-local`

## push in local registry
```shell
docker tag airflow_dwh:2.8.1 192.168.0.146:5555/dwh_group/airflow-build-local:2.8.1
docker push 192.168.0.146:5555/dwh_group/airflow-build-local:2.8.1
```

## save in file
`docker save -o airflow_dwh.tar airflow_dwh:2.8.1`
