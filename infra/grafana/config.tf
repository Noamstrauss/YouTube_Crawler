resource "kubernetes_config_map" "example" {
  metadata {
    name      = "youtube-dashboard"
    namespace = "noams"
    labels = {
      grafana_dashboard = true
    }
  }
  data = {
    "youtube.json" = "${file("${path.module}/youtube.json")}"
  }
}