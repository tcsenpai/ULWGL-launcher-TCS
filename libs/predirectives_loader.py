import os
#import dotenv
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

def set_predirectives(provided_predirectives):
    predirectives = ""
    # Support for the argument (overrides the env var)
    if provided_predirectives is not None and provided_predirectives != "":
        print(f"[INFO] [PREDIRECTIVES] Provided ULWGLDIR={provided_predirectives}")
        predirectives = provided_predirectives
    else:
        print("[INFO] [PREDIRECTIVES] PREDIRECTIVES is not set. Looking for the env var...")
        if "PREDIRECTIVES" not in os.environ:
            print("[WARNING] [PREDIRECTIVES] PREDIRECTIVES is not set. Using default value: '" + predirectives + "'")
        else:
            predirectives = os.environ["PREDIRECTIVES"]
            print(f"[INFO] [PREDIRECTIVES] PREDIRECTIVES={predirectives}")
    return predirectives