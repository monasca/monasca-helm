# Monasca

##  An Open-Source Monitoring as a Service at Scale solution

[Monasca](https://wiki.openstack.org/wiki/Monasca), an [Openstack](https://www.openstack.org/) official project, is a 
scalable monitoring as a service solution. It monitors services and systems by a push model. The Monasca Agent will
collect metrics from each node and push them to the Monasca API. It will then be processed by separate microservices for
storing, alarming and notifications. The architecture can be viewed [here](https://wiki.openstack.org/wiki/File:Monasca-arch-component-diagram.png)

## QuickStart

```bash
$ helm install monasca --name foo --namespace bar
```

## Introduction

This chart bootstraps a [Monasca](https://wiki.openstack.org/wiki/Monasca) deployment on a Kubernetes cluster using the Helm Package manager.

## Prerequisites

- Kubernetes 1.4+

## Installing the Chart

To install the chart with the release name `my-release`:

```bash
$ helm install --name my-release monasca
```

The command deploys Monasca on the Kubernetes cluster in the default configuration. The [configuration](#configuration)
section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
$ helm delete my-release --purge
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the Monasca chart broken down by microservice and their
default values.

### Agent

Parameter | Description | Default
--------- | ----------- | -------
`agent.name` | Agent container name | `agent`
`agent.image.repository` | Agent container image repository | `monasca/agent`
`agent.image.tag` | Agent container image tag | `latest`
`agent.image.pullPolicy` | Agent container image pull policy | `Always`
`agent.log_level` | Log level of agent log files | `WARN`
`agent.keystone.os_username` | Agent Keystone username | `mini-mon`
`agent.keystone.os_user_domain_name` | Agent Keystone user domain | `Default`
`agent.keystone.os_password` | Agent Keystone password | `password`
`agent.keystone.os_project_name` | Agent Keystone project name | `mini-mon`
`agent.keystone.os_project_domain_name` | Agent Keystone project domain | `Default`
`agent.namespace_annotations` | Namespace annotations to set as metrics dimensions | ``
`agent.prometheus.auto_detect_pod_endpoints` | Autodetect Prometheus endpoints for scraping by pods | `true`
`agent.prometheus.auto_detect_service_endpoints` | Autodetect Prometheus endpoints for scraping by services | `true`
`agent.prometheus.kubernetes_labels` | A list of Kubernetes labels to include as dimensions from gathered metrics | `app`
`agent.prometheus.timeout` | The Prometheus endpoint connection timeout | `3`
`agent.kubernetes_api.kubernetes_labels` | A list of Kubernetes labels to include as dimensions from gathered metrics | `app`
`agent.kubernetes_api.timeout` | The K8s API connection timeout | `3`
`agent.kubernetes_api.storage.report` | Report bound pvc capacity metrics per a storage class | `true`
`agent.kubernetes_api.storage.parameter_dimensions` | Storage class parameters as dimensions | ``
`agent.kubernetes.kubernetes_labels` | A list of Kubernetes labels to include as dimensions from gathered metrics | `app`
`agent.kubernetes.timeout` | The cAdvisor/Kubelet connection timeout | `3`
`agent.cadvisor.enabled` | Enable host metrics from cAdvisor | `true`
`agent.cadvisor.timeout` | The cAdvisor connection timeout | `3`
`agent.resources.requests.memory` | Memory request per agent pod | `256Mi`
`agent.resources.requests.cpu` | CPU request per agent pod | `100m`
`agent.resources.limits.memory` | Memory limit per agent pod | `512Mi`
`agent.resources.limits.cpu` | Memory limit per agent pod | `500m`

### API

Parameter | Description | Default
--------- | ----------- | -------
`api.name` | API container name | `api`
`api.image.repository` | API container image repository | `monasca/api`
`api.image.tag` | API container image tag | `master-prometheus`
`api.image.pullPolicy` | API container image pull policy | `Always`
`api.resources.requests.memory` | Memory request per API pod | `256Mi`
`api.resources.requests.cpu` | CPU request per API pod | `250m`
`api.resources.limits.memory` | Memory limit per API pod | `1Gi`
`api.resources.limits.cpu` | Memory limit per API pod | `2000m`
`api.replicaCount` | API pod replica count | `1`
`api.keystone.admin_password` | Keystone admin account password | `secretadmin`
`api.keystone.admin_user` | Keystone admin account user | `admin`
`api.keystone.admin_tenant` | Keystone admin account tenant | `admin`
`api.mysql.user` | MySQL DB username | `monapi`
`api.mysql.password` | MySQL DB password | `password`
`api.influxdb.user` | The influx username | `mon_api`
`api.influxdb.password` | The influx password | `password`
`api.influxdb.database` | The influx database | `mon`
`api.service.port` | API service port | `8070`
`api.service.type` | API service type | `ClusterIP`
`api.service.node_port` | API node port if service type is set to NodePort | ``
`api.logging.log_level_root` | The level of the root logger | `WARN`
`api.logging.log_level_console` | Minimum level for console output | `WARN`
`api.auth_disabled` | Disable Keystone authentication | `false`
`api.authorized_roles` | Roles for admin Users | `user, domainuser, domainadmin, monasca-user`
`api.side_container.enabled` | Enable API side container that collects metrics from the API and exposes as a Prometheus endpoint | `true`
`api.side_container.image.repository` | API side container image repository | `timothyb89/monasca-sidecar`
`api.side_container.image.tag` | API side container image tag | `1.0.0`
`api.side_container.image.pullPolicy` | API side container image pull policy | `Always`
`api.side_container.resources.requests.memory` | Memory request per API side container | `128Mi`
`api.side_container.resources.requests.cpu` | CPU request per API side container | `50m`
`api.side_container.resources.limits.memory` | Memory limit per API side container | `256Mi`
`api.side_container.resources.limits.cpu` | Memory limit per API side container | `100m`


### Client

Parameter | Description | Default
--------- | ----------- | -------
`client.name` | Client container name | `client`
`client.enabled` | Enable deploying client | `false`
`client.image.repository` | Client container image repository | `rbrndt/python-monascaclient`
`client.image.tag` | Client container image tag | `latest`
`client.image.pullPolicy` | Client container image pull policy | `Always`
`client.keystone.os_username` | Keystone user | `mini-mon`
`client.keystone.os_user_domain_name` | Keystone user domain | `Default`
`client.keystone.os_password` | Keystone password | `password`
`client.keystone.os_project_name` | Keystone project name | `mini-mon`
`client.keystone.os_project_domain_name` | Keystone project domain | `Default`

### Forwarder

Parameter | Description | Default
--------- | ----------- | -------
`forwarder.name` | Forwarder container name | `forwarder`
`forwarder.image.repository` | Forwarder container image repository | `monasca/forwarder`
`forwarder.image.tag` | Forwarder container image tag | `master`
`forwarder.image.pullPolicy` | Forwarder container image pull policy | `Always`
`forwarder.enabled` | Enable deploying the forwarder | `false`
`forwarder.replicaCount` | Replica count of Forwarder pods | `1`
`forwarder.logging.debug` | Enable debug logging | `false`
`forwarder.logging.verbose` | Enable verbose logging | `true`
`forwarder.config.remote_api_url` | Versioned monasca api url to forward metrics to | `http://monasca:8070/v2.0`
`forwarder.config.monasca_project_id` | Project ID to forward metrics under | `3564760a3dd44ae9bd6618d442fd758c`
`forwarder.config.use_insecure` | Use insecure when forwarding metrics | `false`
`forwarder.config.monasca_role` | Role to forward metrics under | `monasca-agent`
`forwarder.resources.requests.memory` | Memory request per forwarder pod | `128Mi`
`forwarder.resources.requests.cpu` | CPU request per forwarder pod | `50m`
`forwarder.resources.limits.memory` | Memory limit per forwarder pod | `256Mi`
`forwarder.resources.limits.cpu` | Memory limit per forwarder pod | `100m`

### Grafana

Parameter | Description | Default
--------- | ----------- | -------
`grafana.name` | Grafana container name | `grafana`
`grafana.image.repository` | Grafana container image repository | `monasca/grafana`
`grafana.image.tag` | Grafana container image tag | `4.1.0-pre1-1.0.0`
`grafana.image.pullPolicy` | Grafana container image pull policy | `Always`
`grafana.service.port` | Grafana service port | `3000`
`grafana.service.type` | Grafana service type | `NodePort`
`grafana.resources.requests.memory` | Memory request per grafana pod | `64Mi`
`grafana.resources.requests.cpu` | CPU request per grafana pod | `50m`
`grafana.resources.limits.memory` | Memory limit per grafana pod | `128Mi`
`grafana.resources.limits.cpu` | Memory limit per grafana pod | `100m`

### Kafka

Parameter | Description | Default
--------- | ----------- | -------
`kafka.name` | Kafka container name | `kafka`
`kafka.image.repository` | Kafka container image repository | `monasca/kafka`
`kafka.image.tag` | Kafka container image tag | `0.9.0.1-2.11`
`kafka.image.pullPolicy` | Kafka container image pull policy | `IfNotPresent`
`kafka.resources.requests.memory` | Memory request per kafka pod | `1Gi`
`kafka.resources.requests.cpu` | CPU request per kafka pod | `250m`
`kafka.resources.limits.memory` | Memory limit per kafka pod | `2Gi`
`kafka.resources.limits.cpu` | Memory limit per kafka pod | `2000m`
`kafka.persistence.storageClass` | Kafka storage class | `default`
`kafka.persistence.enabled` | Kafka persistent storage enabled flag | `false`
`kafka.persistence.accessMode` | Kafka persistent storage accessMode | `ReadWriteOnce`
`kafka.persistence.size` | Kafka persistent storage size | `10Gi`
`kafka.topic_config` | Default config args for created topics  | `segment.ms=900000`
`kafka.service.port` | Kafka service port | `9092`
`kafka.service.type` | Kafka service type | `ClusterIP`
`kafka.exporter.enabled` | Kafka exporter enabled flag | `false`
`kafka.exporter.image.repository` | Kafka exporter container image repository | `rbrndt/kafka-prometheus`
`kafka.exporter.image.tag` | Kafka exporter container image tag | `latest`
`kafka.exporter.image.pullPolicy` | Kafka exporter container image pull policy | `IfNotPresent`
`kafka.exporter.port` | Kafka exporter port to expose Promethues metrics on | `7204`


### Keystone

Parameter | Description | Default
--------- | ----------- | -------
`keystone.name` | Keystone container name | `keystone`
`keystone.image.repository` | Keystone container image repository | `monasca/keystone`
`keystone.image.tag` | Keystone container image tag | `1.0.7`
`keystone.image.pullPolicy` | Keystone container image pull policy | `Always`
`keystone.bootstrap.user` | Keystone bootstrap username | `admin`
`keystone.bootstrap.password` | Keystone bootstrap password | `secretadmin`
`keystone.bootstrap.project` | Keystone bootstrap project | `admin`
`keystone.bootstrap.role` | Keystone bootstrap role | `admin`
`keystone.bootstrap.service` | Keystone bootstrap service | `keystone`
`keystone.bootstrap.region` | Keystone bootstrap region | `RegionOne`
`keystone.database_backend` | Keystone backend database | `mysql`
`keystone.mysql.user` | Keystone mysql user | `keystone`
`keystone.mysql.password` | Keystone mysql password | `keystone`
`keystone.mysql.database` | Keystone mysql database | `keystone`
`keystone.replicaCount` | Keystone pod replicas | `1`
`keystone.service.type` | Keystone service type | `ClusterIP`
`keystone.service.port` | Keystone service port | `35357`
`keystone.service.admin_port` | Keystone admin service port | `5000`
`keystone.users.mini_mon.password` | Keystone container image pull policy | `password`
`keystone.users.monasca_agent.password` | Keystone container image pull policy | `password`
`keystone.users.admin.password` | Keystone container image pull policy | `secretadmin`
`keystone.users.demo.password` | Keystone container image pull policy | `secretadmin`
`keystone.users.monasca_read_only.password` | Keystone container image pull policy | `password`
`keystone.resources.requests.memory` | Memory request per keystone pod | `256Mi`
`keystone.resources.requests.cpu` | CPU request per keystone pod | `100m`
`keystone.resources.limits.memory` | Memory limit per keystone pod | `1Gi`
`keystone.resources.limits.cpu` | Memory limit per keystone pod | `500m`

### Notification

Parameter | Description | Default
--------- | ----------- | -------
`notification.name` | Notification container name | `notification`
`notification.image.repository` | Notification container image repository | `monasca/notification`
`notification.image.tag` | Notification container image tag | `master`
`notification.image.pullPolicy` | Notification container image pull policy | `Always`
`notification.replicaCount` | Notification pod replica count | `1`
`notification.mysql.user` | Notification mysql user | `notification`
`notification.mysql.password` | Notification mysql user password | `password`
`notification.log_level` | Notification log level | `WARN`
`notification.plugins` | Notification plugins enabled | `pagerduty,webhook`
`notification.resources.requests.memory` | Memory request per notification pod | `128Mi`
`notification.resources.requests.cpu` | CPU request per notification pod | `50m`
`notification.resources.limits.memory` | Memory limit per notification pod | `256Mi`
`notification.resources.limits.cpu` | Memory limit per notification pod | `100m`

### Persister

Parameter | Description | Default
--------- | ----------- | -------
`persister.name` | Persister container name | `persister`
`persister.image.repository` | Persister container image repository | `monasca/persister`
`persister.image.tag` | Persister container image tag | `master`
`persister.image.pullPolicy` | Persister container image pull policy | `Always`
`persister.replicaCount` | Persister pod replica count | `1`
`persister.influxdb.user` | Persister influx username | `mon_persister`
`persister.influxdb.password` | Persister influx password  | `password`
`persister.influxdb.database` | Persister influx database  | `mon`
`persister.logging.debug` | Persister debug logging enabled  | `false`
`persister.logging.verbose` | Persister verbose logging enabled  | `true`
`persister.resources.requests.memory` | Memory request per persister pod | `128Mi`
`persister.resources.requests.cpu` | CPU request per persister pod | `50m`
`persister.resources.limits.memory` | Memory limit per persister pod | `256Mi`
`persister.resources.limits.cpu` | Memory limit per persister pod | `100m`

### Threshold Engine

Parameter | Description | Default
--------- | ----------- | -------
`thresh.name` | Thresh container name | `thresh`
`thresh.storm_name` | Storm container name | `storm`
`thresh.image.storm.repository` | Storm container image repository | `timothyb89/storm
`thresh.image.storm.tag` | Storm container image tag | `1.0.2.4`
`thresh.image.storm.pullPolicy` | Storm container image pull policy | `Always`
`thresh.image.thresh.repository` | Thresh container image repository | `rbrndt/monasca-thresh`
`thresh.image.thresh.tag` | Thresh container image tag | `latest`
`thresh.image.thresh.pullPolicy` | Thresh container image pull policy | `Always`
`thresh.persistence.storageClass` | Zookeeper storage class | `default`
`thresh.persistence.enabled` | Zookeeper persistent storage enabled flag | `false`
`thresh.persistence.accessMode` | Zookeeper persistent storage accessMode | `ReadWriteOnce`
`thresh.persistence.size` | Zookeeper persistent storage size | `10Gi`
`thresh.mysql.user` | Thresh mysql user | `thresh`
`thresh.mysql.password` | Thresh mysql password | `password`
`thresh.service.nimbus.port` | Storm nimbus service port | `6627`
`thresh.service.nimbus.type` | Storm nimbus service type | `ClusterIP`
`thresh.spout.metricSpoutThreads` | Amount of metric spout threads | `2`
`thresh.spout.metricSpoutTasks` | Amount of metric spout tasks | `2`
`thresh.nimbus_resources.requests.memory` | Memory request per agent pod | `512Mi`
`thresh.nimbus_resources.requests.cpu` | CPU request per agent pod | `100m`
`thresh.nimbus_resources.limits.memory` | Memory limit per agent pod | `2Gi`
`thresh.nimbus_resources.limits.cpu` | Memory limit per agent pod | `500m`
`thresh.supervisor_resources.requests.memory` | Memory request per agent pod | `2Gi`
`thresh.supervisor_resources.requests.cpu` | CPU request per agent pod | `500m`
`thresh.supervisor_resources.limits.memory` | Memory limit per agent pod | `4Gi`
`thresh.supervisor_resources.limits.cpu` | Memory limit per agent pod | `2000m`

### Zookeeper

Parameter | Description | Default
--------- | ----------- | -------
`zookeeper.name` | Zookeeper container name | `zookeeper`
`zookeeper.image.repository` | Zookeeper container image repository | `zookeeper`
`zookeeper.image.tag` | Zookeeper container image tag | `3.3`
`zookeeper.image.pullPolicy` | Zookeeper container image pull policy | `IfNotPresent`
`zookeeper.service.port` | Zookeeper service port | `2181`
`zookeeper.service.type` | Zookeeper service type | `ClusterIP`
`zookeeper.persistence.storageClass` | Zookeeper storage class | `default`
`zookeeper.persistence.enabled` | Zookeeper persistent storage enabled flag | `false`
`zookeeper.persistence.accessMode` | Zookeeper persistent storage accessMode | `ReadWriteOnce`
`zookeeper.persistence.size` | Zookeeper persistent storage size | `10Gi`
`zookeeper.resources.requests.memory` | Memory request per zookeeper pod | `384Mi`
`zookeeper.resources.requests.cpu` | CPU request per zookeeper pod | `100m`
`zookeeper.resources.limits.cpu` | Memory limit per zookeeper pod | `1000m`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```console
$ helm install monasca --name my-release \
    --set persister.replicaCount=4
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the
chart. For example,

```console
$ helm install monasca --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

