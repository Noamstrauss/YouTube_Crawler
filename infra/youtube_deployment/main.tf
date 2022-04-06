#resource "aws_iam_role" "yt_iam_role_ui" {
#  name = "youtube-ui-role"
#  managed_policy_arns = ["arn:aws:iam::aws:policy/AmazonS3FullAccess" ,"arn:aws:iam::aws:policy/IAMFullAccess"]
#  assume_role_policy = jsonencode({
#    Version = "2012-10-17"
#    Statement = [
#      {
#        Action = "sts:AssumeRole"
#        Effect = "Allow"
#        Sid    = ""
#        Principal = {
#          Service = "ec2.amazonaws.com"
#        }
#      },
#    ]
#  })
#
#}

#
#data "aws_iam_policy" "iam_full_accsess" {
#  arn = "arn:aws:iam::aws:policy/IAMFullAccess"
#
#}
#
#data "aws_iam_policy" "s3_full_accsess" {
#  arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
#
#}

#resource "aws_iam_role_policy_attachment" "sto-readonly-role-policy-attach" {
#  role       = aws_iam_role.yt_iam_role_ui.name
#  policy_arn = data.aws_iam_policy.iam_full_accsess.arn
#}
#
#resource "aws_iam_role_policy_attachment" "sto-readonly-role-policy-attach" {
#  role       = aws_iam_role.yt_iam_role_ui.name
#  policy_arn = data.aws_iam_policy.s3_full_accsess.arn
#}


resource "kubernetes_service_account" "yt_service_account_ui" {
  metadata {
    name = "youtube-ui-service-account"
    namespace = var.namespace
    annotations = {
      "eks.amazonaws.com/role-arn": "arn:aws:iam::352708296901:role/Youtube_User_role_noams"
#      "eks.amazonaws.com/role-arn": aws_iam_role.yt_iam_role_ui.arn
      "eks.amazonaws.com/sts-regional-endpoints" = true
    }
  }
  automount_service_account_token = true
}


resource "kubernetes_deployment" "yt_deployment_ui" {
  metadata {
    name = "youtube-ui"
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
          image = "${var.registry_url}/youtube_crawler:latest"
          name  = "youtube-ui"

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
      }
    }
  }
}


resource "kubernetes_service" "yt_service_ui" {
  metadata {
    name = "yt-service-ui"
    namespace = var.namespace
  }
  spec {
    selector = {
      app = kubernetes_deployment.yt_deployment_ui.metadata[0].labels.name
    }
    session_affinity = "ClientIP"
    port {
      port        = 8081
      target_port = 8080
    }

    type = "LoadBalancer"
  }
}