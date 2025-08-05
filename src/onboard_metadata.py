import sys

from src.onboard_dataflowspec import OnboardDataflowspec

import argparse
parser = argparse.ArgumentParser(description="Onboard Dataflowspec Parameters")

parser.add_argument("--catalog_database", type=str, default="", help="Catalog database name")
parser.add_argument("--onboarding_file_path", type=str, default="", help="Path to the onboarding file")
parser.add_argument("--bronze_dataflowspec_table", type=str, default="bronze_dataflowspec_table", help="Bronze Dataflowspec table name")
parser.add_argument("--silver_dataflowspec_table", type=str, default="silver_dataflowspec_table", help="Silver Dataflowspec table name")
parser.add_argument("--env", type=str, default="dev", help="Environment (e.g., dev, prod)")
parser.add_argument("--import_author", type=str, default="", help="Author of the import")

args = parser.parse_args()
catalog_database = args.catalog_database
onboarding_file_path = args.onboarding_file_path
bronze_dataflowspec_table = args.bronze_dataflowspec_table
silver_dataflowspec_table = args.silver_dataflowspec_table
env = args.env
import_author = args.import_author


onboarding_params_map = {}
onboarding_params_map["database"] = catalog_database
onboarding_params_map["onboarding_file_path"] = onboarding_file_path
onboarding_params_map["bronze_dataflowspec_table"] = bronze_dataflowspec_table
onboarding_params_map["silver_dataflowspec_table"] = silver_dataflowspec_table
onboarding_params_map["overwrite"] = "True"
onboarding_params_map["env"] = env
onboarding_params_map["version"] = "v1"
onboarding_params_map["import_author"] = import_author

print(type(onboarding_params_map))
print(f"Onboarding parameters: {onboarding_params_map}")

OnboardDataflowspec(spark, onboarding_params_map, uc_enabled=True).onboard_dataflow_specs()