#output "iam_role_arn" {
#  description = "ARN of IAM role"
#  value       = module.iam_assumable_role_with_oidc.iam_role_arn
#}

#output "identity-oidc-issuer" {
#  value = data.aws_eks_cluster.cluster.identity[0].oidc[0].issuer
#}

#output "load_balancer_hostname" {
#  value = module.youtube-frontend.hostname
#}

output "youtube_frontend_hostname" {
  value = module.route53.youtube_frontend_hostname
}

