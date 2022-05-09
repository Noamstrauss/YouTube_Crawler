
resource "aws_s3_bucket" "yt-files-bucket" {
  bucket = "youtube-crawler-files"
  tags = {
    Name = "youtube-crawler-files"
  }
}

resource "aws_s3_bucket" "tf-state-bucket" {
  bucket = "youtube-tf-state-file"
  tags = {
    Name = "Youtube_tf_state_bucket"
  }
}

resource "aws_s3_bucket_public_access_block" "block" {
  bucket = aws_s3_bucket.tf-state-bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
