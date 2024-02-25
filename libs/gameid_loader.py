#import dotenv
import os

# SECTION Loading the .env file
#dotenv.load_dotenv()

# NOTE Support for game_id
def load_gameid(provided_game_id, default_game_id, ids):
    game_id = default_game_id
    if provided_game_id:
        game_id = provided_game_id
        print(f"[INFO] [GAMEID] Provided GAMEID={game_id}")
    else:
        # We need a valid GAMEID in the .env file in this case
        if "GAMEID" not in os.environ:
            print("[WARNING] [GAMEID] GAMEID is not set. Using default value: '" + str(game_id) + "'")
        else:
            game_id = os.environ["GAMEID"]
            print(f"[INFO] [GAMEID] GAMEID={game_id}")

    # If is not a digit, we will try to load from the ids object
    if not str(game_id).isdigit():
        print(f"[INFO] [GAMEID] {game_id} is not a digit: trying to load from ids.json file")
        if str(game_id) in ids:
            game_id = ids[str(game_id)]
            print(f"[OK] [GAMEID] GAMEID={game_id}")
        else:
            print(f"[WARNING] [GAMEID] {game_id} is not in the ids.json file")
            print("[WARNING] [GAMEID] Defaulting to 0")
            game_id = 0
    print(f"[OK] [GAMEID] GAMEID={game_id}")
    return game_id

