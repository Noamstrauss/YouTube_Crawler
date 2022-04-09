resource "kubernetes_cron_job" "yt_cronjob_back" {
  metadata {
    name      = "youtube-backend"
    namespace = var.namespace
  }
  spec {
    concurrency_policy            = "Replace"
    failed_jobs_history_limit     = 5
    schedule                      = "1 0 * * *"
    starting_deadline_seconds     = 10
    successful_jobs_history_limit = 10
    job_template {
      metadata {
        labels = {
          name = "youtube-backend"
        }
      }
      spec {
        backoff_limit              = 2
        ttl_seconds_after_finished = 10
        template {
          metadata {}
          spec {
            service_account_name = "youtube-service-account-front"
            container {
              name    = "youtube-backend"
              image   = "${var.registry_url}/youtube_crawler:latest"
              command = ["python3", "backend_run.py"]
            }
          }
        }
      }
    }
  }
}