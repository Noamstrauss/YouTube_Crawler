
variable "environment" {}

variable "elastic_ver" {
  type        = string
  default     = ""
  description = "elasticsearch version in grafana datasource info"
}

variable "index_name" {
  default     = ""
  type        = string
  description = "index name to use in elasticsearch datasource"
}

variable "namespace" {
  default     = ""
  description = "namespace to create all resources"
  type        = string
}

variable "grafana_version" {
  default     = ""
  description = ""
  type        = string
}