variable "registry_url" {
  default = ""
  description = "Providing ECR registry url to terraform to pull image"
  type = string
}

variable "namespace" {
  default = ""
  description = "namespace to create all resources"
  type = string
}