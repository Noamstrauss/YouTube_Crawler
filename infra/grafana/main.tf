locals {
  grafana_host = "grafana.${var.environment}.local"
}

data "template_file" "grafana_values" {
  template = file("${path.module}/grafana-values.yaml")

  vars = {
    GRAFANA_HOST = "${local.grafana_host}"
    INDEX_NAME   = var.index_name
    ELASTIC_VER  = var.elastic_ver
  }
}

resource "helm_release" "grafana" {
  name       = "grafana"
  repository = "https://grafana.github.io/helm-charts"
  version    = "6.24.1"
  chart      = "grafana"
  namespace  = "noams"
  timeout    = 1200

  values = [
    data.template_file.grafana_values.rendered
  ]
}