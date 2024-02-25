import os
import json

def set_customvars(provided_customvars,  default_customvars):
    customvars = default_customvars
    # Support for the argument (overrides the env var)
    if provided_customvars:
        try:
            provided_customvars = json.loads(provided_customvars)
        except json.JSONDecodeError:
            print(f"[ERROR] [CUSTOMVARS] Provided CUSTOMVARS={provided_customvars} is not a valid JSON")
            print("[ERROR] [CUSTOMVARS] Defaulting to " + str(customvars))
            provided_customvars = customvars
        print(f"[INFO] [CUSTOMVARS] Provided CUSTOMVARS={provided_customvars}")
        customvars = provided_customvars
    else:
        print("[WARNING] [CUSTOMVARS] CUSTOMVARS is not set. Using default value: '" + str(customvars) + "'")
    # Setting the env vars
    for key, value in customvars.items():
        os.environ[key] = value
    # Force check for the launcher at least
    return customvars