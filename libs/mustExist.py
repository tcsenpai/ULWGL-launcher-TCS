import os
import sys

# Helper
def mustExist(path, fatal=True, is_dir=False):
    # Sanitize the path
    path = os.path.expanduser(path)
    path = path.strip()
    # Determine if the path is absolute or relative
    if not os.path.isabs(path):
        print(f"[INFO] [FILECHECK] {path} is a relative path")
        path = os.path.abspath(path)
        print(f"[INFO] [FILECHECK] Now it is an absolute path: {path}")
    else:
        print(f"[INFO] [FILECHECK] {path} is an absolute path")
    if is_dir:
        print(f"[INFO] [FILECHECK] Checking if '{path}' is a directory")
        if not os.path.isdir(path):
            print(f"[ERROR] [FILECHECK] '{path}' directory does not exist")
            if fatal:
                sys.exit(1)
            else:
                return False
        else:
            print(f"[OK] [FILECHECK] '{path}' is a directory")
            return True
    else:
        if not os.path.exists(path):
            print(f"[ERROR] [FILECHECK] '{path}' does not exist")
            if fatal:
                sys.exit(1)
            else:
                return False
        else:
            print(f"[OK] [FILECHECK] '{path}' exists")
            return True