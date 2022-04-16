locals {
  grafana_host = "grafana.${var.environment}.local"
}

data "template_file" "grafana-values" {
  template = file("${path.module}/grafana-values.yaml")

  vars = {
    GRAFANA_HOST = "${local.grafana_host}"
    INDEX_NAME   = var.index_name
    ELASTIC_VER  = var.elastic_ver
    SMTP_PASSWORD = var.smtp_pass
  }
}

resource "helm_release" "grafana" {
  name       = "grafana"
  repository = "https://grafana.github.io/helm-charts"
  version    = var.grafana_version
  chart      = "grafana"
  namespace  = var.namespace
  timeout    = 1200

  values = [
    data.template_file.grafana-values.rendered
  ]
}