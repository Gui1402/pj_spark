


## Create a bucket for dataproc
resource "google_storage_bucket" "dataproc_bucket" {
provider = google-beta
name     = "${var.bucket_name}-stage-dataproc"
location = var.region
force_destroy = true
}


## Upload of scripts

resource "google_storage_bucket_object" "cnae_job" {
  name   = "jobs/transform_cnae.py"
  bucket = var.bucket_name
  source = "../jobs/transform_cnae.py"
}

resource "google_storage_bucket_object" "estabelecimentos_job" {
  name   = "jobs/transform_estabelecimentos.py"
  bucket = var.bucket_name
  source = "../jobs/transform_estabelecimentos.py"
}


resource "google_storage_bucket_object" "municipios_job" {
  name   = "jobs/transform_municipios.py"
  bucket = var.bucket_name
  source = "../jobs/transform_municipios.py"
}