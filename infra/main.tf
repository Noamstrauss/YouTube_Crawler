terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.21.0"

  name = var.vpc_name
  cidr = var.vpc_cidr

  azs             = var.vpc_azs
  private_subnets = var.vpc_private_subnets
  public_subnets  = var.vpc_public_subnets

  enable_nat_gateway = var.vpc_enable_nat_gateway

  tags = var.vpc_tags
}


resource "aws_instance" "Terraform-Test-ec2" {
  ami           = "ami-002068ed284fb165b"
  instance_type = "t2.micro"

  network_interface {
  network_interface_id = aws_network_interface.foo.id
  device_index         = 0
  }

  

  tags = {
    Name = "ExampleAppServerInstance"
  }



}

