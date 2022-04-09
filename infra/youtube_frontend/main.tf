
data "aws_eks_cluster" "cluster" {
  name = var.cluster_name
}

resource "kubernetes_service_account" "yt_service_account_front" {
  metadata {
    name      = "youtube-service-account-front"
    namespace = var.namespace
    annotations = {
      "eks.amazonaws.com/role-arn" : module.iam_assumable_role_with_oidc.iam_role_arn
      "eks.amazonaws.com/sts-regional-endpoints" = true
    }
  }
  automount_service_account_token = false
}


resource "kubernetes_deployment" "yt_deployment_front" {
  metadata {
    name      = "youtube-front"
    namespace = var.namespace
    labels = {
      name = "youtube-front"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        name = "youtube-front"
      }
    }

    template {
      metadata {
        labels = {
          name = "youtube-front"
        }
      }

      spec {
        container {
          image = "${var.registry_url}/youtube_crawler:latest"
          name = "youtube-front"

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
        service_account_name            = kubernetes_service_account.yt_service_account_front.metadata[0].name
        automount_service_account_token = false
      }
    }
  }
}


#resource "kubernetes_service" "yt_service_front" {
#  metadata {
#    name      = "yt-service-front"
#    namespace = var.namespace
#  }
#  spec {
#    selector = {
#      name = "youtube-front"
#    }
#    port {
#      port        = 8081
#      target_port = 8081
#    }
#
#    type = "NodePort"
#  }
#}