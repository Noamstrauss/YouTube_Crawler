terraform {
  backend "s3" {
    bucket = "youtube-tf-state-files"
    key    = "global/s3/terraform.tfstate"
    region = "eu-north-1"
  }
}