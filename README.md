# AWS Data Engineering Pipeline for Superstore

## Overview

The **AWS Data Engineering Pipeline for Superstore** project demonstrates an end-to-end data engineering workflow using AWS services and tools. This pipeline covers the following components:

- **S3 Bucket Creation:** Managed with Terraform.
- **AWS Glue Catalog Database:** Created to manage metadata.
- **Data Ingestion:** Data downloaded from Kaggle and uploaded to S3 using Python.
- **Data Processing:** Data loaded into AWS Glue Catalog and queried using SQL.
- **Data Visualization:** Transformed data loaded into Power BI to create interactive dashboards.

This project focuses on data from a Superstore dataset, which includes sales, customer, and product information.

## Project Directory Structure



AWS-Data-Engineering-Pipeline-For-Superstore/
│
├── terraform/
│ ├── main.tf
│ ├── glue_catalog.tf
│ ├── fetch_athena_data.py
│ ├── terraform.tfstate
│ ├── terraform.tfstate.backup
│ ├── .terraform/
│ └── .terraform.lock.hcl
│
├── Python-script/
│ ├── upload_to_s3.py
│ └── requirements.txt
│
├── data/
│ ├── Superstore.csv
│ └── archive.zip
│
├── Power-BI-Dashboard/
│ └── PowerBI.pbit
│
├── README.md
└── LICENSE
