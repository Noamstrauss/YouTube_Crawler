module "grafana" {
  source          = "./infra/grafana"
  environment     = var.environment
  elastic_ver     = var.elastic_ver
  index_name      = var.index_name
  namespace       = var.namespace
  grafana_version = var.grafana_version
}

module "s3" {
  source          = "./infra/s3"
}

module "youtube-backend" {
  source          = "./infra/youtube-backend"
  registry_url     = var.registry_url
  cluster_name     = var.cluster_name
  backend_name     = var.backend_name
  namespace       = var.namespace
}

module "youtube-frontend" {
  source          = "./infra/youtube-frontend"
  registry_url     = var.registry_url
  cluster_name     = var.cluster_name
  frontend_name     = var.frontend_name
  namespace       = var.namespace
}











