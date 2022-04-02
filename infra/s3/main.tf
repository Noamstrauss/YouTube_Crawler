#-------------------------------------------------------
#KMS state bucket
#-------------------------------------------------------
#resource "aws_kms_key" "terraform-bucket-key" {
# description             = "This key is used to encrypt bucket objects"
# deletion_window_in_days = 10
# enable_key_rotation     = true
#}
#
#resource "aws_kms_alias" "key-alias" {
# name          = "alias/terraform-bucket-key1"
# target_key_id = aws_kms_key.terraform-bucket-key.key_id
#}
#-------------------------------------------------------
#s3 state bucket
#-------------------------------------------------------
resource "aws_s3_bucket" "tf_state_bucket" {
  bucket = "youtube-tf-state-files"
  tags = {
    Name        = "Youtube_tf_state_bucket"
  }
}

resource "aws_s3_bucket_public_access_block" "block" {
 bucket = aws_s3_bucket.tf_state_bucket.id

 block_public_acls       = true
 block_public_policy     = true
 ignore_public_acls      = true
 restrict_public_buckets = true
}

output "s3_bucket_arn" {
  value       = aws_s3_bucket.tf_state_bucket.arn
  description = "The ARN of the S3 bucket"
}
#-------------------------------------------------------
#DynamoDB state table
#-------------------------------------------------------
#resource "aws_dynamodb_table" "terraform-state" {
# name           = "terraform-state"
# read_capacity  = 20
# write_capacity = 20
# hash_key       = "LockID"
#
# attribute {
#   name = "LockID"
#   type = "S"
# }
#}