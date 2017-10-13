### Zookeeper Configurations

Parameter | Description | Default
--------- | ----------- | -------
`image.repository` | Zookeeper container image repository | `zookeeper`
`image.tag` | Zookeeper container image tag | `3.3`
`image.pullPolicy` | Zookeeper container image pull policy | `IfNotPresent`
`service.type` | Zookeeper service type | `ClusterIP`
`persistence.storageClass` | Zookeeper storage class | `default`
`persistence.enabled` | Zookeeper persistent storage enabled flag | `false`
`persistence.accessMode` | Zookeeper persistent storage accessMode | `ReadWriteOnce`
`persistence.size` | Zookeeper persistent storage size | `10Gi`
`resources.requests.memory` | Memory request per zookeeper pod | `256Mi`
`resources.requests.cpu` | CPU request per zookeeper pod | `100m`
`resources.limits.cpu` | Memory limit per zookeeper pod | `1000m`
`resources.limits.memory` | Memory limit per zookeeper pod | `512Mi`
`java.max_ram_fraction` | Fraction of Ram to deveote to Heap (1/n) | `2`
