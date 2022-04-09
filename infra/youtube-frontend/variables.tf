variable "registry_url" {
  default     = ""
  description = "Providing ECR registry url to terraform to pull image"
  type        = string
}

variable "namespace" {
  default     = ""
  description = "Namespace to create all resources"
  type        = string
}

variable "cluster_name" {
  default     = ""
  description = "EKS cluster name"
  type        = string
}

variable "frontend_name" {
  default     = ""
  description = "Frontend name for resources"
  type        = string
}