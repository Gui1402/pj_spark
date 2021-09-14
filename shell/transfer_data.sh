#! /bin/bash

# create a bucket and get file from data host
bucket_name=desafio-final-318823
gsutil mb -c standard -l us-east1 gs://${bucket_name}
gsutil -m cp -r gs://desafio-final/* gs://${bucket_name}/raw/