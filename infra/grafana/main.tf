locals {
  grafana_host = "grafana.${var.environment}.local"
}

resource "kubernetes_namespace" "grafana" {
  metadata {
    name = "grafana"
  }
}

data "template_file" "grafana-values" {
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
  version    = var.grafana_version
  chart      = "grafana"
  namespace  = kubernetes_namespace.grafana.metadata[0].name
  timeout    = 1200
  depends_on = [kubernetes_namespace.grafana]

  values = [
    data.template_file.grafana-values.rendered
  ]
}