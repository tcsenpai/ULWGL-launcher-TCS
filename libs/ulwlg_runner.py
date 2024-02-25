import os

def ulwlg_run(executable_path, ulwlg_dir, proton_dir, wineprefix, game_id):

    executable_dir = os.path.dirname(executable_path)

    os.environ["ULWGL_ID"] = str(game_id)
    os.environ["STEAM_COMPAT_APP_ID"] = "0" # REVIEW Is this ok?
    os.environ["SteamAppId"] = os.environ["STEAM_COMPAT_APP_ID"]
    os.environ["SteamGameId"] = os.environ["STEAM_COMPAT_APP_ID"]

    os.environ["PROTON_VERB"] = "waitforexitandrun"

    os.environ["STEAM_COMPAT_CLIENT_INSTALL_PATH"] = ""
    os.environ["STEAM_COMPAT_DATA_PATH"] = wineprefix
    os.environ["STEAM_COMPAT_SHADER_PATH"] = wineprefix + "/shadercache"

    os.environ["PROTON_CRASH_REPORT_DIR"] = "/tmp/ULWGL_crashreports"
    os.environ["FONTCONFIG_PATH"] = ""

    os.environ["STEAM_COMPAT_TOOL_PATHS"] = proton_dir + ":" + ulwlg_dir
    os.environ["STEAM_COMPAT_MOUNTS"] = proton_dir + ":" + ulwlg_dir

    if os.environ.get("STEAM_COMPAT_INSTALL_PATH") is None:
        os.environ["STEAM_COMPAT_INSTALL_PATH"] = executable_dir
    

    # Composing the command
    composed_command = (
        ulwlg_dir
        + "/ULWGL --verb=waitforexitandrun"
        + "  -- "
        + proton_dir
        + "/proton waitforexitandrun "
        + executable_path
        + "$@"
    )

    print("[ULWGL_RUNNER] Composed command: " + composed_command)


    os.system(composed_command)
