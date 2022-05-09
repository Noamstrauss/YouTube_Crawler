output "s3_bucket_arn" {
  value       = aws_s3_bucket.tf-state-bucket.arn
  description = "The ARN of the S3 bucket"
}