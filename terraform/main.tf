provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_data_bucket" {
  bucket = "my-unique-bucket-2024-07-15"
  acl    = "private"
}


resource "aws_glue_catalog_database" "my_database" {
  name = "new_database"
}