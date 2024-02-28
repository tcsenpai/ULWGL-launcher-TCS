import os

def wine_run(executable_path, wine_dir):
    # NOTE The wineprefix is set in the environment variable WINEPREFIX and is not needed as an argument
    print("[WINE_RUNNER] Running " + executable_path + " with Wine version: ")
    os.system(wine_dir + "/bin/wine --version")
    executable_dir = os.path.dirname(executable_path)
    if executable_dir == "":
        executable_dir = "."
    # Composing the command
    composed_command = ( "cd " + executable_dir + " && " + wine_dir + "/bin/wine " + executable_path + "$@")
    print("[WINE_RUNNER] Composed command: " + composed_command)
    os.system(composed_command)
