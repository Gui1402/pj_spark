# Specify the GCP Provider
provider "google-beta" {
project = var.project
region  = var.region
}


terraform {
  backend "gcs" {
    bucket = "terraform-state-edc"
    prefix = "state/igti/edc/mod1/terraform.tfstate"
  }

}