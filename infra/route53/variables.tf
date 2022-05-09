variable "frontend_name" {
  default     = ""
  description = "Frontend name for resources"
  type        = string
}

variable "load_balancer_hostname" {}

variable "hosted_zone_name" {}

variable "region_zone_id" {}