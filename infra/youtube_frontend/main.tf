
data "aws_eks_cluster" "cluster" {
  name = var.cluster_name
}

resource "kubernetes_service_account" "yt_service_account_ui" {
  metadata {
    name      = "youtube-ui-service-account"
    namespace = var.namespace
    annotations = {
      "eks.amazonaws.com/role-arn" : module.iam_assumable_role_with_oidc.iam_role_arn
      "eks.amazonaws.com/sts-regional-endpoints" = true
    }
  }
  automount_service_account_token = false
}


resource "kubernetes_deployment" "yt_deployment_ui" {
  metadata {
    name      = "youtube-ui"
    namespace = var.namespace
    labels = {
      name = "youtube-ui"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        name = "youtube-ui"
      }
    }

    template {
      metadata {
        labels = {
          name = "youtube-ui"
        }
      }

      spec {
        container {
          image           = "${var.registry_url}/youtube_crawler:latest"
          name            = "youtube-ui"

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
        service_account_name = kubernetes_service_account.yt_service_account_ui.metadata[0].name
        automount_service_account_token = false
      }
    }
  }
}


resource "kubernetes_service" "yt_service_ui" {
  metadata {
    name      = "yt-service-ui"
    namespace = var.namespace
  }
  spec {
    selector = {
      name = "youtube-ui"
    }
    port {
      port        = 8081
      target_port = 8081
    }

    type = "NodePort"
  }
}