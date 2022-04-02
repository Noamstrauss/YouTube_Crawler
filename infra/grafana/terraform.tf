terraform {
 backend "s3" {
   bucket         = "youtube-tf-state-files"
   key            = "state/youtube/terraform.tfstate"
   region         = "eu-north-1"
   encrypt        = true
 }
}