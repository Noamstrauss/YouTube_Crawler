#
#output "iam_role_arn" {
#  description = "ARN of IAM role"
#  value       = module.iam_assumable_role_with_oidc.iam_role_arn
#}
#
#
#
#output "identity-oidc-issuer" {
#  value = data.aws_eks_cluster.cluster.identity[0].oidc[0].issuer
#}

output "hostname" {
  value = kubernetes_service_v1.example.status.0.load_balancer.0.ingress.0.hostname
}

#output "youtube_frontend_hostname_fqdn" {
#  value = aws_route53_record.www.fqdn
#}