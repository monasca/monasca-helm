# Monasca Helm

This repo contains Helm charts for Monasca and its dependencies. Each chart release is hosted on
[monasca.io](http://monasca.io) via github pages.

## Quick Start

To install Monasca in Kubernetes you can follow the following steps:

```bash
$ helm repo add monasca http://monasca.io/monasca-helm
$ helm install monasca/monasca --name monasca --namespace monitoring
```

It may take several minutes to download the container images.

If you have already added the helm repo make sure you update it before installing monasca to ensure you get the latest
version

```bash
$ helm repo update
```

By default Monasca will monitor pod workloads, basic Kubernetes Health and autodetect Prometheus endpoints.

### Local Development Environment
For local development we use [minikube](https://github.com/kubernetes/minikube) for bringing up Kubernetes to deploy
Monasca on.

### Accessing Data via Grafana

Apart of the Monasca install is Grafana with default Kubernetes graphs. This can be accessed by port-forwarding the
grafana service to localhost.

Setting up grafana port-forward:
```bash
$ kubectl get pods -n monitoring -l component=grafana
$ kubectl port-forward {{ grafana_pod_name_from_output_above }} -n monitoring 3000
```

After the above is set up you can visit [grafana](http://localhost:3000) with the default credentials mini-mon/password

For more details on configuring the Monasca chart you can refer to the chart's [README](monasca/README.md) and for
general details around Monasca in Kubernetes you can refer to [monasca.io](http://monasca.io/docs/kubernetes.html)

The monasca influxdb chart is created from https://github.com/kubernetes/charts/tree/master/stable/influxdb
