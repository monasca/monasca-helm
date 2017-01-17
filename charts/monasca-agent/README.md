# Monasca Agent Helm

Helm Chart to install and configure[Monasca Agent](https://github.com/openstack/monasca-agent) for[Monasca](https://wiki.openstack.org/wiki/Monasca)

## Introduction
Will deploy a daemonset that will monitoring each container and pod on each node as well as the host itself and a
deployment that will monitor the Kubernetes API.

## Configuration

The following table shows the configurable parameters of the Monasca agent chart and their defaults.

| Parameter | Description | Default |
| --------- | ----------- | ------- |
| `image` | Image for the agent to pull down | `hoppalm/monasca-agent:latest` |
| `keystone.os_auth_url` | Auth url for keystone | `http://keystone:35357/v3/` |
| `keystone.os_username` | Username for authenticating with keystone | `mini-mon` |
| `keystone.os_user_domain_name` | User domain name for username scoping | `Default` |
| `keystone.os_password` | Password for authenticating with keystone | `password` |
| `keystone.os_project_name` | Specifies the name of the Keystone project name to store the metrics under, defaults to users default project. | `mini-mon` |
| `monasca_url` | URL for monasca to send metrics to | `http://monasca:8070/v2.0` |
