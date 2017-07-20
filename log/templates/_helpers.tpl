{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a fully qualified log-api name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "log_api.fullname" -}}
{{- printf "%s-%s" .Release.Name "api" | trunc 63 -}}
{{- end -}}

{{/*
Create a fully qualified log-metrics name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "log_metrics.fullname" -}}
{{- printf "%s-%s" .Release.Name "metrics" | trunc 63 -}}
{{- end -}}

{{/*
Create a fully qualified log-transformer name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "log_transformer.fullname" -}}
{{- printf "%s-%s" .Release.Name "transformer" | trunc 63 -}}
{{- end -}}

{{/*
Create a fully qualified kafka name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "kafka.fullname" -}}
{{- printf "%s-%s" .Release.Name "kafka" | trunc 63 -}}
{{- end -}}

{{/*
Create a fully qualified zookeeper name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "zookeeper.fullname" -}}
{{- printf "%s-%s" .Release.Name "zookeeper" | trunc 63 -}}
{{- end -}}
