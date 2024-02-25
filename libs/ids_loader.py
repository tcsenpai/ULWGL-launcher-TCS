#import dotenv
import os
import json
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
# dotenv.load_dotenv()

# NOTE Loading ids.json file
def load_ids(provided_ids, default_ids, default_ids_json_path):
    ids_json_path = default_ids_json_path
    ids = default_ids
    # Support for the argument (overrides the env var)
    if not provided_ids:
        if "IDS_JSON" in os.environ:
            ids_json_path = os.environ["IDS_JSON"]
            print(f"[INFO] [IDS] IDS_JSON={ids_json_path}")
        else:
            print(f"[WARNING] [IDS] IDS_JSON is not set. Using default value: {default_ids_json_path}")
    if provided_ids:
        ids_json_path = provided_ids
        if not mustExist(ids_json_path, fatal=False):
            print(f"[WARNING] [IDS] Using default value: {default_ids_json_path}")
            ids_json_path = default_ids_json_path
        print(f"[OK] [IDS] IDS_JSON={ids_json_path}")
        ids =  json.loads(open(ids_json_path, "r").read())
    # Support for non existing ids.json file
    if not mustExist(ids_json_path, fatal=False):
        print(f"[WARNING] [IDS] {ids_json_path} does not exist")
        print("[WARNING] [IDS] Defaulting to 0 will be used in case of non digit game_id")
        ids = {}
    return ids, ids_json_path