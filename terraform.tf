terraform {
  backend "s3" {
    bucket = "youtube-tf-state-file"
    key    = "state/global-terraform/terraform.tfstate"
    region = "eu-north-1"
  }
}