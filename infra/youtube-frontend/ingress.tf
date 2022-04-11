resource "kubernetes_service_v1" "example" {
  metadata {
    name = "ingress-service"
    namespace = var.namespace
  }
  spec {
    selector = {
      name = "youtube-frontend"
    }
    port {
      port        = 80
      target_port = 8081
      protocol    = "TCP"
    }
    type = "NodePort"
  }
}

resource "kubernetes_ingress_v1" "frontend" {
  wait_for_load_balancer = true
  metadata {
    name = "frontend-ingress"
    namespace = var.namespace
    labels = {
      name = "front-ingress"
    }
  }
  spec {
    ingress_class_name = "nginx"
    rule {
      http {
        path {
          path = "/*"
          backend {
            service {
              name = kubernetes_service_v1.example.metadata.0.name
              port {
                number = kubernetes_service_v1.example.spec.0.port.0.port
              }
            }
          }
        }
      }
    }
  }
}

## Display load balancer hostname (typically present in AWS)
#output "load_balancer_hostname" {
#  value = kubernetes_ingress_v1.example.status.0.load_balancer.0.ingress.0.hostname
#}
#
## Display load balancer IP (typically present in GCP, or using Nginx ingress controller)
#output "load_balancer_ip" {
#  value = kubernetes_ingress_v1.example.status.0.load_balancer.0.ingress.0.ip
#}