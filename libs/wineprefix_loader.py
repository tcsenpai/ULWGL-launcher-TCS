#import dotenv
import os
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

# NOTE Setting the Wine prefix with a fallback
def set_wineprefix(provided_wineprefix, default_wine_prefix):
    wine_prefix = default_wine_prefix
    # Support for the argument (overrides the env var)
    if provided_wineprefix:
        wine_prefix = provided_wineprefix
        print(f"[INFO] [WINEPREFIX] Provided WINEPREFIX={wine_prefix}")
        if not mustExist(wine_prefix, fatal=False):
            print(f"[WARNING] [WINEPREFIX] {wine_prefix} does not exist")
            print("[WARNING] [WINEPREFIX] Defaulting to " + default_wine_prefix)
            wine_prefix = default_wine_prefix
    else:
        # We need a valid WINEPREFIX in the .env file in this case
        if "WINEPREFIX" not in os.environ:
            print("[WARNING] [WINEPREFIX] WINEPREFIX is not set. Using default value: '" + wine_prefix + "'")
        else:
            wine_prefix = os.environ["WINEPREFIX"]
            print(f"[INFO] [WINEPREFIX] WINEPREFIX={wine_prefix}")
    # We need this to exist
    mustExist(wine_prefix)
    print(f"[OK] [WINEPREFIX] WINEPREFIX={wine_prefix}")
    return wine_prefix
