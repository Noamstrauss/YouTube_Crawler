
data "aws_route53_zone" "this" {
  name = var.hosted_zone_name
}

resource "aws_route53_record" "record" {
  zone_id = data.aws_route53_zone.this.zone_id
  name    = "youtube"
  type    = "A"

  alias {
    name                   = var.load_balancer_hostname
    zone_id                = var.region_zone_id
    evaluate_target_health = false
  }
}