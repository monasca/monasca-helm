### Kafka Configuration parameters

Parameter | Description | Default
--------- | ----------- | -------
`image.repository` | Kafka container image repository | `monasca/kafka`
`image.tag` | Kafka container image tag | `0.9.0.1-2.11-1.1.4`
`image.pullPolicy` | Kafka container image pull policy | `IfNotPresent`
`resources.requests.memory` | Memory request per kafka pod | `1Gi`
`resources.requests.cpu` | CPU request per kafka pod | `250m`
`resources.limits.memory` | Memory limit per kafka pod | `2Gi`
`resources.limits.cpu` | Memory limit per kafka pod | `2000m`
`persistence.storageClass` | Kafka storage class | `default`
`persistence.enabled` | Kafka persistent storage enabled flag | `false`
`persistence.accessMode` | Kafka persistent storage accessMode | `ReadWriteOnce`
`persistence.size` | Kafka persistent storage size | `10Gi`
`topic_config` | Default config args for created topics  | `segment.ms=900000`
`service.port` | Kafka service port | `9092`
`service.type` | Kafka service type | `ClusterIP`
`exporter.enabled` | Kafka exporter enabled flag | `false`
`exporter.image.repository` | Kafka exporter container image repository | `rbrndt/kafka-prometheus`
`exporter.image.tag` | Kafka exporter container image tag | `latest`
`exporter.image.pullPolicy` | Kafka exporter container image pull policy | `IfNotPresent`
`exporter.port` | Kafka exporter port to expose Promethues metrics on | `7204`
`stack_size` | JVM stack size | `1024k`
`memory_ratio` | Ratio of memory to reserve for the JVM out of cgroup limit | `.85`