#provider "kubernetes" {
#  config_path = ".kube"
#}

provider "helm" {
  kubernetes {
    config_path = ".kube"
  }
}