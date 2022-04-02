terraform {
 backend "s3" {
   bucket         = "youtube-tf-state-files"
   key            = "state/s3/terraform.tfstate"
   region         = "eu-north-1"
   encrypt        = true
   kms_key_id     = "alias/terraform-bucket-key"

 }
}