#! /bin/bash
bucket_name=desafio-final-318823

gsutil -m cp -r gs://desafio-final/* gs://${bucket_name}/raw/