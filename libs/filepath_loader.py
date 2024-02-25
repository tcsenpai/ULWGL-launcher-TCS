#import dotenv
import os
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

# NOTE Sanity check for the game path
def set_filepath(provided_filepath, LAUNCHDIR):
    # Support for the argument (overrides the env var)
    if not provided_filepath:
        if "FILEPATH" not in os.environ:
            print("[ERROR] [FILEPATH] FILEPATH is not set. Exiting...")
            exit(1)
        else:
            provided_filepath = os.environ["FILEPATH"]
    # Get the path to the file
    # Distinguish between absolute and relative paths
    if os.path.isabs(provided_filepath):
        filepath = provided_filepath
    else:
        filepath = os.path.join(LAUNCHDIR, provided_filepath)

    # Check if the file exists
    if not mustExist(filepath, fatal=False):
        print(f"[WARNING] [FILEPATH] File not found: {filepath}")
        print("[WARNING] [FILEPATH] ulwgl will be launched with the argument provided but it may not work.")
        print("[INFO] [FILEPATH] Disregard this message if you are using an internal or custom binary (e.g. winecfg...)")
        filepath=provided_filepath
    print("[OK] [FILEPATH] " + filepath + "\n")

    # Quick space sanity check
    if " " in filepath:
        print(f"[WARNING] [FILEPATH] {filepath} contains spaces")
        print("[WARNING] [FILEPATH] This may cause issues with the launcher")
        print("[WARNING] [FILEPATH] Consider renaming the file or moving it to a different location")
        print("[QUICK FIX] [FILEPATH] Trying to escape the spaces")
        filepath = filepath.replace(" ", "\ ")
        print(f"[QUICK FIX] [FILEPATH] {filepath}\n")
    return filepath
