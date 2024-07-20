# AWS Data Engineering Pipeline for Superstore

## Overview

The **AWS Data Engineering Pipeline for Superstore** project showcases an end-to-end data engineering workflow using AWS services and tools. The pipeline includes:

- **S3 Bucket Creation:** Managed with Terraform.
- **AWS Glue Catalog Database:** Created to manage metadata.
- **Data Ingestion:** Downloaded from Kaggle and uploaded to S3 using Python.
- **Data Processing:** Loaded into AWS Glue Catalog and queried using SQL.
- **Data Visualization:** Transformed data loaded into Power BI to create interactive dashboards.

This project focuses on data from a Superstore dataset, which includes sales, customer, and product information.

## Project Components

### 1. **Terraform Configuration**

- **S3 Bucket:** Configurations to create an AWS S3 bucket.
- **Glue Catalog Database:** Configurations to create an AWS Glue catalog database.

### 2. **Python Scripts**

- **Data Upload Script:** `upload_to_s3.py` - Downloads data from Kaggle and uploads it to the S3 bucket.

### 3. **AWS Glue**

- **ETL Jobs:** Scripts and configurations to process data using AWS Glue and run SQL queries.

### 4. **Power BI Dashboard**

- **Dashboard File:** Contains interactive visualizations based on the transformed data.

AWS-Data-Engineering-Pipeline-For-Superstore/
│
├── terraform/
│   ├── main.tf
│   ├── glue_catalog.tf
│   ├── fetch_athena_data.py
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   ├── .terraform/
│   └── .terraform.lock.hcl
│
├── Python-script/
│   ├── upload_to_s3.py
│   └── requirements.txt
│
├── data/
│   ├── Superstore.csv
│   └── archive.zip
│
├── Power-BI-Dashboard/
│   └── PowerBI.pbit
│
├── README.md
└── LICENSE

