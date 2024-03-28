def create_launcher(
        game_id,
        proton_path,
        wine_prefix,
        ulwgl_dir,
        predirectives,
        filepath,
        postdirectives,
        loaded_customvars,
        use_wine
):
    """
    Creates a launcher for the game
    :param game_id: The game id
    :param proton_path: The proton path
    :param wine_prefix: The wine prefix
    :param ulwgl_dir: The ulwgl dir
    :param predirectives: The predirectives
    :param filepath: The filepath
    :param postdirectives: The postdirectives
    :param loaded_customvars: The loaded custom vars
    :param use_wine: If we are using wine or not
    :return: None
    """
    # Creating the launcher
    launcher = f"""
# This file was created by ULWGL
PROTONPATH="{proton_path}"
USE_WINE="{use_wine}"
WINEPREFIX="{wine_prefix}"
GAMEID="{game_id}"
ULWGLDIR="{ulwgl_dir}"
PREDIRECTIVES="{predirectives}"
FILEPATH="{filepath}"
POSTDIRECTIVES="{postdirectives}"
CUSTOMVARS='{loaded_customvars}'
"""
    
    # Writing the launcher
    with open(f"{ulwgl_dir}/launcher.uwine", "w") as file:
        file.write(launcher)