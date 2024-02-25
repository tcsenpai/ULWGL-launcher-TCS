# ULWGL-LAUNCHER-TCS ( ⾣ UWINE )

The final wrapper for ULWGL (and its launcher) has come to town.

Play and run Windows software with Proton without Steam in a (maybe a couple of) click.

![Hello world](https://raw.githubusercontent.com/tcsenpai/UWINE/main/screenshot.png)

## What is ULWGL-LAUNCHER-TCS ( ⾣ UWINE )

UWINE is a wrapper around ULWGL designed to help as many users as possible to run WIndows software (included but not limited to games) using Proton (and its flavors like ProtonGE) without Steam client needed.

## Credits and License

This software is distributed under the MIT license.

The original ULWGL-Launcher repository and its creators (https://github.com/Open-Wine-Components/ULWGL-launcher) are to be credited for all the amazing work they are doing.

This is just an humble wrapper designed for the following reason:

- I am lazy and I don't want to tinker with the terminal each time I want to play a game

- Many people are lazy

- Many others are non tech-savy

## Enormous Disclaimer (IMPORTANT)

- My only goal is to provide the same level of comfort I have to others

- ALL The work done by the OpenWineComponents deserves a statue or more than one

- Being an experimental version of ULWGL-Launcher this can be prone to errors

## ⭐ Features

- Uses libs/ulwgl_runner.py instead of the provided ulwgl-run for a cleaner approach

- Can run programs as simply as "uwine program.exe" (or "uwine winecfg" for internal tools)

- Fully customizable through both a human readable CLI interface and a practical format for `env` files

- Can execute _launchers_ by using the above `env` files mechanism with "uwine -l launcher_of_game"

- Can be configured through both the `env` file and the CLI interface together (with the CLI interface overriding the `env` file)

- Can be used to "Open with..."

- The Launcher provided can be used to "Open with..." too

- Is modular and so is readable

- Can be expanded easily

- I use it daily

- Is quite nice

## Install

_NOTE: the current release has been tested with 0.1 RC3 release in mind and thus that's the version included in laucher/_

### ⚙ Prerequisites

- Any Proton version; GE-Proton is highly recommended

#### Getting Proton

You are advised to either use tools like ProtonUp (and its -QT flavor) or to download the latest release from https://github.com/GloriousEggroll/proton-ge-custom/releases and extract it in a folder that you will use as PROTONPATH

- Python

- Not needed of my machine but: ensure to read launcher/Original_README.md to understand ULWGL Launcher prerequisites

### ⏬ Get UWINE

#### ⚙ Download and Configuration

- `git clone https://github.com/tcsenpai/ULWGL-launcher-TCS`

- `cd ULWGL-launcher-TCS`

- `pip install -r requirements.txt`

- Now take a moment to have a look at the .env file. It contains some useful tips. You can add custom paths to it, for example, Steam usually install its instances in subfolders of `$HOME/.steam/steam/compatibilitytools.d`

- The .env file works as a launcher that helps you run your programs in the easiest way possible. While is not really needed (see below), the provided example shows how UWINE can run with almost 0 configuration

#### 🕮 A brief explanation: skip if you can't be bothered

It is important to understand how UWINE works. The 'uwine' executable has to fill the following variables:

- PROTONPATH

  - string pointing to your custom Proton installation (see Prerequisites)
  - defaults to [script_dir]/protons

- WINEPREFIX

  - string pointing to a custom prefix for wine (aka where savegames and programs are installed)
  - defaults to [script_dir]/PREFIX and creates a new one if needed

- GAMEID

  - integer representing the GameID in the ULWGL Database
  - defaults to 0 which should work for the majority of the apps

- IDS

  - string pointing to a .json file containing mappings of game names to game ids
  - defaults to [script_dir]/ids.json
  - if it doesn't exist, the mapping will be empty

- ULWGLDIR

  - string pointing to your ULWGLDIR installation
  - defaults to [script_dir]/launcher which is perfectly fine if extract ULWGL_Launcher there (not in a subfoldr)

- FILEPATH

  - string pointing to the file to execute
  - if not specified, it must be specified from the CLI (see below)

- CUSTOMVARS

  - dictionary-like string (JSON compatible) defining any environmental variable you want to set
  - can be omitted if you don't need it

- PREDIRECTIVES

  - string containing parameters and arguments to be *prepended* to the command (e.g. gamescope)
  - defaults to ""

- POSTDIRECTIVES

  - string containing parameters and arguments to be *appended* to the command (e.g. -dx11)
  - defaults to ""
  - can be set using the `-a` flag

**_TIP: You should consider using ProtonUp (or ProtonUp-QT for KDE users) to help you easily install Proton instances in the 'protons' folder or wherever you like the most_**

#### 🧧 Bonus: CUSTOMVARS

While adding custom environmental variables both in your shell or in the env file is supported, UWINE has a mechanism that is designed to help you in setting custom system variables.

By editing the `env` file you want to use, you can add:

```json
  CUSTOMVARS='{
    "YOUR_VAR": "YOUR_VALUE"
  }'
```

The above syntax allows UWINE to present you in a nicer and more organized way your final command.

### 🚀 Launch

Once launched, UWINE will quickly sets the above variables based on either the `.env` file (or the one provided) or/and the command line arguments

After some basic checks (like if the file exists, if PROTONPATH is set...), UWINE will look for the `ulwgl-run` binary and use it to launch the program with the above mentioned variables.

Thats why the next section is really important.

## Command Line Arguments & Launchers

The preferred way to use UWINE is by creating `env` files following the above format and then just run `uwine` to load them.

### Load the .env file

`uwine`

This command will try to load the `.env` file in the script directory.

### Load a custom env file

`uwine -l [your_env_file]`

This command will try to load the env file specified.

### Specify your variables (or mix the two)

`uwine -h`

This command will show you the following:

```bash
usage: uwine [-h] [-l ENVFILE] [-g GAMEID] [-p PROTONPATH] [-i IDS] [-w WINEPREFIX] [-u ULWGLDIR] [-a ADDITIONALARGS] [-v] [filepath]

ULWGL Launcher Wrapper for human beings

positional arguments:
  filepath              Path to the file to be launched

options:
  -h, --help            show this help message and exit
  -l ENVFILE, --load ENVFILE
                        Load a specific env file
  -g GAMEID, --game-id GAMEID
                        Game ID to be used
  -p PROTONPATH, --proton-path PROTONPATH
                        Path to the Proton installation
  -i IDS, --ids-json IDS
                        Path to the ids.json file
  -w WINEPREFIX, --wine-prefix WINEPREFIX
                        Path to the Wine prefix
  -u ULWGLDIR, --ulwgl ULWGLDIR
                        Path to the ULWGL installation
  -a ADDITIONALARGS, --additionalargs ADDITIONALARGS
                        Additional arguments to be passed to the software (as a string)
  -v, --version         show program's version number and exit

```

The help file is self explanatory.

For example, a possible usage is:

`uwine winecfg -u "/your/hdd/data/ulwgl" -w "/your/hdd/data/ulwgl/PREFIX/" -p "/your/hdd/data/ulwgl/protons/GE-Proton8-32/"`

This will launch the built-in `winecfg` program using the specified variables.

Another example could be:

`uwine -l mygame`

Where `mygame` must be a valid env file as described above.

#### About ADDITIONALARGS

It is often necessary to add additional arguments to your programs (e.g. `-dx11`) to modify their behavior. To help in this, you can simply use the `-a` option specifying a string that will be appended to your launched program.

For example, to launch Palworld with `-dx11`:

`uwine Palworld.exe -a "-dx11"`

Multiple arguments can be chained together in the string such as:

`uwine game.exe -a "-dx11 --skip-launcher"`

You can also set the additional arguments from the env.example file as POSTDIRECTIVES (see above for explanations).

### Optional: the ids.json file

As the excellent tutorial on the ULWGL Launcher repository page explains, ULWGL aims to build a complete, open database of games with the relative protonfixes that should be applied automatically by the launcher itself.

As UWINE's intent is to simplify things, you can skip this part and us the launcher with the default game id `0`. Anyway, experimental game id support is included.

At the moment the `ids.json` contains just an example of how it works.

`{ "gamename": gameid }`

The syntax is simple as the above example. Baldur's Gate 3 has been included as an example. Launching UWINE with:

`uwine game.exe -g bg3`

Will instruct UWINE to look for "bg3" in the ids.json file. If not found, it will default to `0`. You can also do:

`uwine game.exe -g 12345`

You can also use the .env file as per the env.example.

Where 12345 is a custom game id that you can either invent (but why) or look up on the ULWGL database (https://ulwgl.openwinecomponents.org/).

Howeaver, this is considered quite experimental for both the projects.

### Optional: add this directory to $PATH

To quickly use UWINE, is recommended to add the directory you are using (the ULWGL Launcher directory containing uwine) to the $PATH variable.

You can add this:

`PATH="$PATH:/your/path/to/the/ULWGL/launcher/directory"`

To either your `.profile`, `.bashrc` or equivalent configuration file.

### ??? Profit

Done! You should be able to run

`uwine any_program.exe` from anywhere.

### ✋ Handy stuff: Open With

This repository offers also a preconfigured launcher (`uwine.desktop`) that should work on every modern linux DM/WM. You can put it anywhere (e.g. in your applications menu) and you can configure .exe and .msi (and any other) files to "Open with..." uwine.

You can also set `.uwine` files to open with `uwine -l ` or use the given launcher (`uwine_launcher.desktop`) to launch env files.

If this does not work, you can simply "Open with..." and add a custom command called 'uwine' / 'uwine -l' that launches in the terminal.

### ✋ Handy stuff 2: AIO Package

An All-in-One package is on the way and contains the official ULWGL release tested with uwine and uwine installed in it.

Is not as funny but it should be even more straightforward.

## Updates

I will try to keep launcher/ in line with the latest ULWGL_Launcher repository version.

If for any reason I am unable to do so or you want to do it manually, you can simply (in this directory):

``` bash
# Backup the current launcher
mv launcher launcher_bak
# Clone the latest version of ULWGL_Launcher
git clone https://github.com/Open-Wine-Components/ULWGL-launcher
# Set it as the default launcher
mv ULWGL-Launcher launcher
```
Some of the files won't be used but you can safely ignore them (it is just a little bit messier).

## Issues, bugs, dragons

This is even more experimental than ULWGL itself. Bugs are to be expected.

Please open issues or pr if you encounter some.

Before doing that, though, please ensure that the problem is with UWINE and not with ULWGL or Proton.

For example: some Steam games may fail to launch complaining about the Steam Client not being found. That's an ULWGL / Proton problem. Surely is not an UWINE problem. Probably. Anyway....

### Testing environment and compatibility

This software has been tested on the following system (a laptop):

- KUbuntu 23.10 with Plasma on Wayland

- Python 3.11

- Kernel 6.5, Kernel 6.7.4 Xanmod x64v3 and 6.7.5 Xanmod x64v3

- ProtonGE-8.32 both in protons local folder and in .steam default folder

- ProtonUp 2.8.2

- CPU AMD 7 7730U (Zen 3) with integrated RADEON Graphics (RADV Renoir)

- 16GB RAM (14GB + 2GB VRAM)

- Both _bash_ and _xonsh_ shells

- Both external and internal SSDs

## Roadmap

- Testing, testing, testing

- Finding bugs, fixing bugs

- Full support to all ULWGL features

- Testing again for safety measure

I will use (as I am doing) UWINE for my daily gaming experience, so I will update it accordingly. Feel free (please) to do the same.

## Call to test

We need you! Everybody needs you! Linux itself needs you!

Yes, you.

And by that I mean: please stress test and help me improve this software so that we can help the ULWGL team focusing on the important stuff.

An era of gaming, an era of universal Proton compatibility is coming.

Be part of it!

## Disclaimer

Sorry for any mistake. It wasn't inentional.

## License

MIT License.
