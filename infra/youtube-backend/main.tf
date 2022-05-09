
resource "kubernetes_cron_job" "yt-cronjob-back_deleter" {
  metadata {
    name      = var.backend_name
    namespace = var.namespace
  }
  spec {
    concurrency_policy            = "Allow"
    failed_jobs_history_limit     = 1
    schedule                      = "*/3 * * * *"
    starting_deadline_seconds     = 10
    successful_jobs_history_limit = 0
    job_template {
      metadata {
        labels = {
          name = var.backend_name
        }
      }
      spec {
        backoff_limit              = 10
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
              image_pull_policy = "Always"
            }
          }
        }
      }
    }
  }
}


#resource "kubernetes_cron_job" "yt-cronjob-back_checker" {
#  metadata {
#    name      = "youtube-backend-checker"
#    namespace = var.namespace
#  }
#  spec {
#    concurrency_policy            = "Allow"
#    failed_jobs_history_limit     = 1
#    schedule                      = "*/3 * * * *"
#    successful_jobs_history_limit = 0
#    job_template {
#      metadata {
#        labels = {
#          name = "youtube-backend-checker"
#        }
#      }
#      spec {
#        backoff_limit              = 10
#        ttl_seconds_after_finished = 300
#        template {
#          metadata {}
#          spec {
#            service_account_name            = "youtube-service-account"
#            automount_service_account_token = false
#            restart_policy                  = "OnFailure"
#            container {
#              name              = "youtube-backend-checker"
#              image             = "${var.registry_url}/youtube_crawler:latest"
#              command           = ["python3", "backend/get_users_tags.py"]
#              image_pull_policy = "IfNotPresent"
#            }
#          }
#        }
#      }
#    }
#  }
#}