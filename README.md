# Created a Data Pipeline using AWS 

## Overview

The AWS DataPipeline for project demonstrates an end-to-end data engineering workflow using AWS services and tools. This pipeline covers the following components:

- **S3 Bucket Creation:** Managed with Terraform.
- **AWS Glue Catalog Database:** Created to manage metadata.
- **Data Ingestion:** Data downloaded from Kaggle and uploaded to S3 using Python.
- **Data Processing:** Data loaded into AWS Glue Catalog and queried using SQL.
- **Data Visualization:** Transformed data loaded into Power BI to create interactive dashboards.

This project focuses on data from a Superstore dataset, which includes sales, customer, and product information.

### **`terraform/` Directory**

Contains Terraform configurations and state files used to provision AWS resources.

- **`main.tf`**: Main Terraform configuration for setting up AWS infrastructure.
- **`glue_catalog.tf`**: Terraform configuration for setting up the AWS Glue Catalog database.
- **`fetch_athena_data.py`**: Python script for querying data from Athena (if applicable).
- **`terraform.tfstate`**: Terraform state file tracking the current state of your infrastructure.
- **`terraform.tfstate.backup`**: Backup of the Terraform state file.
- **`.terraform/`**: Directory created by Terraform containing plugin binaries and workspace data.
- **`.terraform.lock.hcl`**: Lock file to ensure consistent dependency versions.

### **`Python-script/` Directory**

Contains Python scripts used for data processing.

- **`upload_to_s3.py`**: Script to download data from Kaggle and upload it to the S3 bucket.
- **`requirements.txt`**: List of Python dependencies required by `upload_to_s3.py`.

### **`data/` Directory**

Contains data files used in the project.

- **`Superstore.csv`**: Sample data file for testing or reference.
- **`archive.zip`**: Archive of data files.

### **`Power-BI-Dashboard/` Directory**

Contains files related to Power BI dashboards.

- **`PowerBI.pbit`**: Power BI template file for creating dashboards and visualizations.





