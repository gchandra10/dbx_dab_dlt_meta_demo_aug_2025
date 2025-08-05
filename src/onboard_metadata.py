import sys

from src.onboard_dataflowspec import OnboardDataflowspec

onboarding_params_map = {
    "database": "gannychan.default",
    "onboarding_file_path": "/Volumes/gannychan/default/dlt-meta-conf/onboarding_people.json",
    "bronze_dataflowspec_table": "bronze_dataflowspec_table", 
    "silver_dataflowspec_table": "silver_dataflowspec_table", 
    "overwrite": "True",
    "env": "dev",
    "version": "v1",
    "import_author": "Ganny Chan",
}

print(type(onboarding_params_map))
print(f"Onboarding parameters: {onboarding_params_map}")

OnboardDataflowspec(spark, onboarding_params_map, uc_enabled=True).onboard_dataflow_specs()