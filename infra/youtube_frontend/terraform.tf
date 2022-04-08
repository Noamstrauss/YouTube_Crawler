terraform {
  backend "s3" {
    bucket = "youtube-tf-state-files"
    key    = "state/youtube_ui/terraform.tfstate"
    region = "eu-north-1"

  }
}