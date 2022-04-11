resource "kubernetes_namespace" "ingress_nginx" {
  metadata {
    name = "ingress-nginx"
  }
}

resource "helm_release" "ingress_nginx" {
  name       = "ingress-nginx"
  chart      = "ingress-nginx"
  version    = "4.0.16"
  repository = "https://kubernetes.github.io/ingress-nginx"
  namespace  = "ingress-nginx"
  values = [
    <<EOF
rbac:
  create: true
controller:
  ingressClassResource:
    name: nginx
    enabled: true
    default: true
    controllerValue: "k8s.io/ingress-nginx"
  replicaCount: 1
  autoscaling:
    minReplicas: 2
    maxReplicas: 4
  publishService:
    enabled: true
  containerPort:
    http: 80
    https: 443
  metrics:
    enabled: true
  resources:
    requests:
      cpu: 100m
      memory: 100Mi
    limits:
      cpu: 500m
      memory: 500Mi
EOF
  ]
  wait = false
}
