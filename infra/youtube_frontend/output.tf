
output "iam_role_arn" {
  description = "ARN of IAM role"
  value       = module.iam_assumable_role_with_oidc.iam_role_arn
}



output "identity-oidc-issuer" {
  value = data.aws_eks_cluster.example.identity[0].oidc[0].issuer
}