# AWS Batch Processing Pipeline

This repository contains the architecture and implementation details for a batch data processing pipeline on AWS. This pipeline ingests data from a REST API, stores it in Amazon S3, and processes it using AWS Glue, PySpark, and Amazon Athena. The pipeline was created with AWS services to ensure scalability, security, and cost efficiency.


## Architecture Overview
![aws_batch_processing](https://github.com/user-attachments/assets/59365244-b43b-4a38-870c-99f9e4e4a872)
The pipeline follows these main steps:

1. **Data Ingestion**:
   - Data is collected from a REST API and ingested into Amazon S3.
   
2. **Data Storage**:
   - The ingested data is stored in Amazon S3 as raw files, which can be processed later for analytical or ETL purposes.
   
3. **Metadata Cataloging**:
   - AWS Glue Crawlers are used to scan the data in S3, infer the schema, and populate the AWS Glue Data Catalog, making it available for querying.

4. **Data Transformation and Analysis**:
   - Data is transformed using AWS Glue with PySpark jobs. This step cleans and prepares the data for further analysis.
   - Amazon Athena is used to query the processed data, enabling users to run ad-hoc queries on the data in S3.

5. **Access and Permissions**:
   - AWS IAM ensures secure access control for all resources within the pipeline.
   - AWS CloudFormation is used to provision and manage the infrastructure, making it easy to set up and replicate the pipeline.

## Components

- **Amazon S3**: Storage for raw and processed data.
- **REST API**: Source of data ingested into the pipeline.
- **AWS Glue**:
  - **Crawler**: Scans data in S3 and automatically updates the Glue Data Catalog.
  - **Glue Catalog**: Stores metadata, making it accessible for ETL jobs and Athena queries.
  - **PySpark Jobs**: Data transformation and processing tasks.
- **Amazon Athena**: Runs SQL-based queries on the data stored in S3, leveraging the Glue Data Catalog.
- **AWS IAM**: Provides secure access and permissions management.
- **AWS CloudFormation**: Manages and provisions pipeline resources.

## Data Flow

1. **Data ingestion** from the REST API stores raw data in Amazon S3.
2. **Glue Crawler** scans S3, infers the schema, and updates the Glue Catalog.
3. **Glue PySpark jobs** process and transform the data, making it ready for querying.
4. **Athena** uses the Glue Catalog to query processed data, with results stored back in S3.
5. **IAM and CloudFormation** manage security and infrastructure provisioning.

## How to Use

1. **Ingest Data**: Configure the REST API data source to push data to Amazon S3.
2. **Run Crawler**: Set up and execute the AWS Glue Crawler to catalog the ingested data.
3. **Transform Data**: Use AWS Glue PySpark jobs for data transformations.
4. **Query Data**: Utilize Amazon Athena to run SQL queries on the processed data.
