
data "aws_eks_cluster_auth" "example" {
  name = var.cluster_name
}

#resource "kubernetes_service" "example" {
#  metadata {
#    name      = "yt-service-frontend"
#    namespace = var.namespace
#  }
#  spec {
#    selector = {
#      name = "youtube-frontend"
#    }
#    port {
#      port        = 8081
#      target_port = 8081
#      protocol    = "TCP"
#
#    }
#    type = "ClusterIP"
#  }
#}
#
## Create a local variable for the load balancer name.
#locals {
#  lb_name = split("-", split(".", kubernetes_service.example.status.0.load_balancer.0.ingress.0.hostname).0).0
#}
#
## Read information about the load balancer using the AWS provider.
#data "aws_elb" "example" {
#  name = local.lb_name
#}
#
#output "load_balancer_name" {
#  value = local.lb_name
#}
#
#output "load_balancer_hostname" {
#  value = kubernetes_service.example.status.0.load_balancer.0.ingress.0.hostname
#}
#
#output "load_balancer_info" {
#  value = data.aws_elb.example
#}