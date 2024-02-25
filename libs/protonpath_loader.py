import os
#import dotenv
import libs.mustExist as sanity
mustExist = sanity.mustExist

# SECTION Loading the .env file
#dotenv.load_dotenv()

# NOTE Setting the Proton path with a fallback
def set_protonpath(provided_protonpath, default_proton_path, UWINEDIR):
    proton_path = default_proton_path
    # Support for the argument (overrides the env var)
    if provided_protonpath:
        proton_path = provided_protonpath
        print(f"[INFO] Provided PROTONPATH={proton_path}")
        # Distinguish between absolute and relative paths to support versioning
        if not os.path.isabs(proton_path):
            print(f"[INFO] {proton_path} is a relative path")
            print(f"[INFO] Appending {UWINEDIR}/protons/ to {proton_path}")
            proton_path = os.path.join(UWINEDIR, "protons", proton_path)
            print("[INFO] Now it is an absolute path: " + proton_path)
        if not mustExist(proton_path, fatal=False):
            print(f"[WARNING] {proton_path} does not exist")
            print("[WARNING] Defaulting to " + default_proton_path)
            proton_path = default_proton_path
    else:
        # We need a valid PROTONPATH in the .env file in this case
        if "PROTONPATH" not in os.environ:
            print("[WARNING] PROTONPATH is not set. Using default value: '" + proton_path + "'")
        else:
            proton_path = os.environ["PROTONPATH"]
            print(f"[INFO] PROTONPATH={proton_path}")
    # We need this to exist
    mustExist(proton_path)
    print(f"[OK] PROTONPATH={proton_path}")
    return proton_path