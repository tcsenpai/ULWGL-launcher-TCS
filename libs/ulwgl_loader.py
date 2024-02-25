import os
#import dotenv
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

def set_ulwgldir(provided_ulwgldir, default_ulwgl_dir):
    ulwgl_dir = default_ulwgl_dir
    # Support for the argument (overrides the env var)
    if provided_ulwgldir:
        print(f"[INFO] [ULWGLDIR] Provided ULWGLDIR={provided_ulwgldir}")
        if not mustExist(provided_ulwgldir, fatal=False, is_dir=True):
            print(f"[WARNING] [ULWGLDIR] {provided_ulwgldir} does not exist")
            print("[WARNING] [ULWGLDIR] Defaulting to " + default_ulwgl_dir)
            ulwgl_dir = default_ulwgl_dir
        else:
            ulwgl_dir = provided_ulwgldir
    else:
        # We need a valid UWINEDIR in the .env file in this case
        if "ULWLGDIR" not in os.environ:
            print("[WARNING] [ULWGLDIR] ULWGLDIR is not set. Using default value: '" + ulwgl_dir + "'")
        else:
            ulwgl_dir = os.environ["ULWLGDIR"]
            print(f"[INFO] [ULWGLDIR] ULWGLDIR={ulwgl_dir}")

    # Force check for the launcher at least
    mustExist(ulwgl_dir + "/ULWGL")
    return ulwgl_dir