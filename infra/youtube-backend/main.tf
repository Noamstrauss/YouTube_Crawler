
resource "kubernetes_cron_job" "yt-cronjob-back" {
  metadata {
    name      = var.backend_name
    namespace = var.namespace
  }
  spec {
    concurrency_policy            = "Replace"
    failed_jobs_history_limit     = 1
    schedule                      = "*/15 * * * *"
    starting_deadline_seconds     = 200
    successful_jobs_history_limit = 0
    job_template {
      metadata {
        labels = {
          name = var.backend_name
        }
      }
      spec {
        backoff_limit              = 2
        ttl_seconds_after_finished = 100
        template {
          metadata {}
          spec {
            service_account_name            = "youtube-service-account"
            automount_service_account_token = false
            restart_policy                  = "OnFailure"
            container {
              name              = var.backend_name
              image             = "${var.registry_url}/youtube_crawler:latest"
              command           = ["python3", "backend_run.py"]
              image_pull_policy = "IfNotPresent"
            }
          }
        }
      }
    }
  }
}