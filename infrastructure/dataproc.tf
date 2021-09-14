resource "google_dataproc_cluster" "mycluster" {
  provider = google-beta
  name   = "dproc-cluster-${var.project}"
  region = var.region


  cluster_config {
    staging_bucket = google_storage_bucket.dataproc_bucket.id

    master_config {
      num_instances = 1
      machine_type  = "n1-standard-4"
      disk_config {
        boot_disk_type    = "pd-ssd"
        boot_disk_size_gb = 250
      }
    }

    worker_config {
      num_instances    = 0
    }

    preemptible_worker_config {
      num_instances = 0
    }

    endpoint_config {
    enable_http_port_access = "true"
    }


    # Override or set some custom properties
    software_config {
      image_version = "2.0-debian10"
      override_properties = {
        "dataproc:dataproc.allow.zero.workers" = "true"
      }
      optional_components = ["JUPYTER"]
    }

    gce_cluster_config {
      tags = ["igti", "edc"]
      # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
      service_account = "edc-igti@gcp-learning-318823.iam.gserviceaccount.com"
      service_account_scopes = [
        "cloud-platform"
      ]
    }

    initialization_action {
      script      = "gs://dataproc-initialization-actions/stackdriver/stackdriver.sh"
      timeout_sec = 500
    }

    # You can define multiple initialization_action blocks

  }

}


# Submit an example pyspark job to a dataproc cluster
resource "google_dataproc_job" "pyspark_cnae" {
  provider = google-beta
  region       = google_dataproc_cluster.mycluster.region
  force_delete = true
  placement {
    cluster_name = google_dataproc_cluster.mycluster.name
  }

  pyspark_config {
    main_python_file_uri = "gs://${var.bucket_name}/jobs/transform_cnae.py"
    properties = {
      "spark.logConf" = "true"
    }
  }
}



resource "google_dataproc_job" "pyspark_municipios" {
  provider = google-beta
  region       = google_dataproc_cluster.mycluster.region
  force_delete = true
  placement {
    cluster_name = google_dataproc_cluster.mycluster.name
  }

  pyspark_config {
    main_python_file_uri = "gs://${var.bucket_name}/jobs/transform_municipios.py"
    properties = {
      "spark.logConf" = "true"
    }
  }
}



resource "google_dataproc_job" "pyspark_estabelecimentos" {
  provider = google-beta
  region       = google_dataproc_cluster.mycluster.region
  force_delete = true
  placement {
    cluster_name = google_dataproc_cluster.mycluster.name
  }

  pyspark_config {
    main_python_file_uri = "gs://${var.bucket_name}/jobs/transform_estabelecimentos.py"
    properties = {
      "spark.logConf" = "true"
    }
  }
}


