# Example Terraform starter for GCP
provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {}
variable "region" {}

output "project" {
  value = var.project_id
}
