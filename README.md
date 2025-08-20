# Demo: Using Databricks DLT META with DAB in VSCode

## Objective

This project demonstrates how to deploy a DLT-META project using DABS and VSCode.

**It covers the following use cases:**

- Deploying Bronze, Silver, and Silver Fanout jobs & pipelines
- Running pipelines in both Dev and Prod modes
- Adding custom columns and metadata to Bronze tables
- Creating HashKeys on selected deterministic columns
- Implementing SCD Type 1 to Silver tables
- Applying DLT (LDP) expectations to filter data in Silver tables

## Pre-requisite

**Windows Users**

```
SET DATABRICKS_HOST=<>
```

**Mac Users**

```
export DATABRICKS_HOST=<>
```

Assumes you have latest Databricks CLI installed and configured to your workspace.
  
   ```
      databricks configure --profile DEFAULT
   ```
Create two volumes dlt-meta-conf and dlt-meta-data under your catalog > schema
  - Upload the contents of conf including dqe into dlt-meta-conf volume
  - Upload the people.csv from ```resources/data``` into dlt-meta-data volume

Update the ```resources/var_people.yml``` file with your Dev and Prod details. If you are not testing Prod, then have the same details for Prod also.

## Details on files

resources/

   **people_job.yml**: Creates a JOB for onboarding bronze and silver metadata.

   **people_pipeline.yml**: Creates the bronze-silver pipelines.

   **var_people.yml**: Contains all configurable values.

conf/

   **onboarding_bronze_silver_metadata_people.json**: contains onboarding specifications for bronze-silver tables.

   **onboarding_silver_fanout_metadata_people.json**: contains onboarding specifications for multiple (fanout) silver tables.

   **silver_queries_people.json**: contains the select expression for various silver tables.

conf/dqe/

   **dqe_silver_prople.json**: sample Expectations to filter bad data into Silver tables.


## Run the Jobs/Pipelines

- To Validate & deploy a development copy of this project, type:
   
   ```
   databricks bundle validate
   ```
    ```
    databricks bundle deploy --target dev
    ```

   ```
   $ databricks bundle deploy --target prod
   ```

- Run the onboard job to build the Bronze and Silver onboarding schema
   
   ```
   databricks bundle run onboard_people -t dev
   ```

- Run the pipelines job to run Bronze and Silver pipelines

   ```
   databricks bundle run execute_pipelines_people -t dev
   ```

- Destroy the Pipelines

   ```
   databricks bundle destroy -t dev
   ```

   ```
   databricks bundle destroy -t prod
   ```

