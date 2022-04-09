module "iam_assumable_role_with_oidc" {
  source  = "terraform-aws-modules/iam/aws//modules/iam-assumable-role-with-oidc"
  version = "~> 4"

  create_role = true

  role_name = "role-with-oidc-noams"

  tags = {
    Role = "role-with-oidc-noams"
  }
  provider_url = data.aws_eks_cluster.cluster.identity[0].oidc[0].issuer

  role_policy_arns           = ["arn:aws:iam::aws:policy/AmazonS3FullAccess"]
  number_of_role_policy_arns = 1
}

resource "aws_iam_role_policy_attachment" "IAMFullAccess-policy-attach" {
  role       = module.iam_assumable_role_with_oidc.iam_role_name
  policy_arn = "arn:aws:iam::aws:policy/IAMFullAccess"
}

resource "kubernetes_service_account" "yt-service-account" {
  metadata {
    name      = "youtube-service-account"
    namespace = var.namespace
    annotations = {
      "eks.amazonaws.com/role-arn" : module.iam_assumable_role_with_oidc.iam_role_arn
      "eks.amazonaws.com/sts-regional-endpoints" = true
    }
  }
  automount_service_account_token = false
}

