
data "aws_eks_cluster" "cluster" {
  name = var.cluster_name
}

data "kubernetes_service_account" "service-account" {
  metadata {
    namespace = var.namespace
    name      = "youtube-service-account"
  }
}


resource "kubernetes_deployment" "yt-deployment-front" {
  metadata {
    name      = var.frontend_name
    namespace = var.namespace
    labels = {
      name = var.frontend_name
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        name = var.frontend_name
      }
    }

    template {
      metadata {
        labels = {
          name = var.frontend_name
        }
      }

      spec {
        container {
          image = "${var.registry_url}/youtube_crawler:latest"
          name  = var.frontend_name
          port {
            container_port = 8081
          }

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "0.2"
              memory = "50Mi"
            }
          }
        }
        service_account_name            = data.kubernetes_service_account.service-account.metadata[0].name
        automount_service_account_token = false
      }
    }
  }
}
