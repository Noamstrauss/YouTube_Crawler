
output "youtube_frontend_hostname" {
  value = "http://${aws_route53_record.record.fqdn}"
}

