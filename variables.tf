
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

variable "registry_url" {
  default     = ""
  description = "Providing ECR registry url to terraform to pull image"
  type        = string
}

variable "cluster_name" {
  default     = ""
  description = "EKS cluster name"
  type        = string
}


variable "backend_name" {
  default     = ""
  description = "Backend name for resources"
  type        = string

}

variable "frontend_name" {
  default     = ""
  description = "Frontend name for resources"
  type        = string
}


