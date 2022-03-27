resource "kubernetes_deployment" "yt_deployment_user" {
  metadata {
    namespace = "noams"
    labels = {
      name = "noams-youtube-user"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
         name = "noams-youtube-user"
      }
    }

    template {
      metadata {
        labels = {
         name = "noams-youtube-user"
        }
      }

      spec {
        container {
          image = var.imagetag
          name  = "youtube-user"

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}


resource "kubernetes_service" "yt_service_user" {
  metadata {
    name = "terraform-example"
  }
  spec {
    selector = {
      app = kubernetes_deployment.yt_deployment_user.metadata.labels.name
    }
    session_affinity = "ClientIP"
    port {
      port        = 8080
      target_port = 80
    }

    type = "LoadBalancer"
  }
}