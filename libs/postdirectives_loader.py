import os
#import dotenv
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

def set_postdirectives(provided_postdirectives):
    postdirectives = ""
    # Support for the argument (overrides the env var)
    if provided_postdirectives is not None and provided_postdirectives != "":
        print(f"[INFO] [POSTDIRECTIVES] Provided ULWGLDIR={provided_postdirectives}")
        postdirectives = provided_postdirectives
    else:
        print("[INFO] [POSTDIRECTIVES] POSTDIRECTIVES is not set. Looking for the env var...")
        if "POSTDIRECTIVES" not in os.environ:
            print("[WARNING] [POSTDIRECTIVES] POSTDIRECTIVES is not set. Using default value: '" + postdirectives + "'")
        else:
            postdirectives = os.environ["POSTDIRECTIVES"]
            print(f"[INFO] [POSTDIRECTIVES] POSTDIRECTIVES={postdirectives}")
    return postdirectives