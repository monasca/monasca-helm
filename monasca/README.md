# Monasca

##  An Open-Source Monitoring as a Service at Scale solution

[Monasca](https://wiki.openstack.org/wiki/Monasca), an
[Openstack](https://www.openstack.org/) official project, is a scalable
monitoring as a service solution. It monitors services and systems by a push
model. The Monasca Agent will collect metrics from each node and push them to
the Monasca API. It will then be processed by separate microservices for
storing, alarming and notifications. The architecture can be viewed
[here](https://wiki.openstack.org/wiki/File:Monasca-arch-component-diagram.png)

## QuickStart

```bash
$ helm repo add monasca http://monasca.io/monasca-helm-repo
$ helm install monasca/monasca --name monasca --namespace monitoring
```

## Introduction

This chart bootstraps a [Monasca](https://wiki.openstack.org/wiki/Monasca)
deployment on a Kubernetes cluster using the Helm Package manager.

## Prerequisites

- Kubernetes 1.4+

## Installing the Chart

Monasca can either be install from the [monasca.io](https://monasca.io/) helm repo or by source.

### Installing via Helm repo (recommended)

```bash
$ helm repo add monasca http://monasca.io/monasca-helm-repo
$ helm install monasca/monasca --name monasca --namespace monitoring
```

### Installing via source

```bash
$ helm repo add monasca http://monasca.io/monasca-helm-repo
$ helm dependency update monasca
$ helm install monasca --name monasca --namespace monitoring
```

Either option will bring Monasca on the Kubernetes cluster with the default
configuration. The [configuration](#configuration) section lists the parameters
that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
$ helm delete my-release --purge
```

The command removes all the Kubernetes components associated with the chart and
deletes the release.

### Default monitoring

By default Monasca will monitor pod workloads (CPU, Network, Memory, etc.) and Kubernetes health.

It will also autodetect Prometheus Endpoints by looking for the following annotations on services and pods

* prometheus.io/scrape: Only scrape pods that have a value of 'true'
* prometheus.io/path: If the metrics path is not '/metrics' override this.
* prometheus.io/port: Scrape the pod on the indicated port instead of the default of '9102'.

More information on our monitoring within in Kubernetes can be found on
[monasca.io Kubernetes](http://monasca.io/docs/kubernetes.html)

## Configuration

The following tables lists the configurable parameters of the Monasca chart
broken down by microservice and their default values.

Specify each parameter using the `--set key=value[,key=value]` argument to
`helm install`. For example,

```console
$ helm install monasca --name my-release \
    --set persister.replicaCount=4
```

Alternatively, a YAML file that specifies the values for the below parameters
can be provided while installing the chart. For example,

```console
$ helm install monasca --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

### Agent

Parameter | Description | Default
--------- | ----------- | -------
`agent.name` | Agent container name | `agent`
`agent.image.repository` | Agent container image repository | `monasca/agent`
`agent.image.tag` | Agent container image tag | `latest`
`agent.image.pullPolicy` | Agent container image pull policy | `Always`
`agent.insecure` | Insecure connection to Keystone and Monasca API | `False`
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


### MySQL

Parameter | Description | Default
----------|-------------|--------
`mysql.imageTag` | Tag to use from `library/mysql` | `5.6`
`mysql.imagePullPolicy` | K8s pull policy for mysql image | `IfNotPresent`
`mysql.persistence.enabled` | If `true`, enable persistent storage | `false`
`mysql.persistence.storageClass` | K8s storage class to use for persistence | `default`
`mysql.persistence.accessMode` | PVC access mode | `ReadWriteOnce`
`mysql.persistence.size` | PVC request size | `10Gi`
`mysql.resources.requests.memory` | Memory request | `256Mi`
`mysql.resources.requests.cpu` | CPU request | `100m`
`mysql.resources.limits.memory` | Memory limit | `1Gi`
`mysql.resources.limits.cpu` | CPU limit | `500m`
`mysql.users.keystone.username` | Keystone MySQL username | `keystone`
`mysql.users.keystone.password` | Keystone MySQL password | `keystone`
`mysql.users.api.username` | API MySQL username | `monapi`
`mysql.users.api.password` | API MySQL password | `password`
`mysql.users.notification.username` | Notification MySQL username | `notification`
`mysql.users.notification.password` | Notification MySQL password | `password`
`mysql.users.thresh.username` | Thresh MySQL username | `thresh`
`mysql.users.thresh.password` | Thresh MySQL password | `password`


### MySQL Init

Parameter | Description | Default
--------- | ----------- | -------
`mysql_init.image.repository` | docker repository for mysql-init | `monasca/mysql-init`
`mysql_init.image.tag` | Docker image tag | `1.2.0`
`mysql_init.image.pullPolicy` | Kubernetes pull polify for image | `IfNotPresent`
`mysql_init.disable_remote_root` | If `true`, disable root account after init finishes successfully | `true`


### Notification

Parameter | Description | Default
--------- | ----------- | -------
`notification.name` | Notification container name | `notification`
`notification.image.repository` | Notification container image repository | `monasca/notification`
`notification.image.tag` | Notification container image tag | `master`
`notification.image.pullPolicy` | Notification container image pull policy | `Always`
`notification.replicaCount` | Notification pod replica count | `1`
`notification.log_level` | Notification log level | `WARN`
`notification.plugins` | Notification plugins enabled | `pagerduty,webhook`
`notification.plugin_config.email.defined` | Notification email plugin configuration is defined | `false`
`notification.plugin_config.email.server` | SMTP server address | ``
`notification.plugin_config.email.port` | SMTP server port | ``
`notification.plugin_config.email.user` | SMTP username | ``
`notification.plugin_config.email.password` | SMTP password | ``
`notification.plugin_config.email.from_addr` | "from" field for emails sent, e.g. "Name" <name@example.com> | ``
`notification.plugin_config.webhook.timeout` | Webhook timeout | `5`
`notification.plugin_config.hipchat.ssl_certs` | Path to SSL certs | ``
`notification.plugin_config.hipchat.timeout` | Hipchat timeout | `5`
`notification.plugin_config.hipchat.insecure` | Insecure when sending to Hipchat | ``
`notification.plugin_config.hipchat.proxy` |  if set, use the given HTTP(S) proxy server to send Hipchat notifications | ``
`notification.plugin_config.slack.timeout` | Notification slack timeout | `5`
`notification.plugin_config.slack.certs` | Path to Slack certs | ``
`notification.plugin_config.slack.insecure` | Insecure when sending to Slack | ``
`notification.plugin_config.slack.proxy` |  if set, use the given HTTP(S) proxy server to send Slack notifications | ``
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
`thresh.image.storm.pullPolicy` | Storm container image pull policy | `Always`
`thresh.image.repository` | Thresh container image repository | `monasca/thresh`
`thresh.image.tag` | Thresh container image tag | `master`
`thresh.image.pullPolicy` | Thresh container image pull policy | `Always`
`thresh.secretSuffix` | MySQL secret suffix | `mysql-thresh-secret`
`thresh.spout.metricSpoutThreads` | Amount of metric spout threads | `2`
`thresh.spout.metricSpoutTasks` | Amount of metric spout tasks | `2`
`thresh.wait.retries` | Number of startup connection attempts to make before giving up | `24`
`thresh.wait.delay` | Seconds to wait between retries | `5`
`thresh.wait.timeout` | Attempt connection timeout in seconds | `10`

Storm-specific options are documented in the
[Storm chart](https://github.com/hpcloud-mon/monasca-helm/tree/master/storm).
