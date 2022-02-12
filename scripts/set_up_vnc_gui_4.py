#!/usr/bin/env python3


from pathlib import Path
import sys
import os

MAIN_DIR = Path(sys.argv[0]).parent.parent

VNC_CONFIGS_DIR = MAIN_DIR.joinpath("vnc_configs")

with open(VNC_CONFIGS_DIR.joinpath("gnome.conf")) as conf:
    gnome_startup_script = conf.read()

with open(VNC_CONFIGS_DIR.joinpath("xfce.conf")) as conf:
    xfce_startup_script = conf.read()

configs = {
    "GNOME": {
        "number": 1,
        "startup_script": gnome_startup_script,
    },
    "XFCE": {
        "number": 2,
        "startup_script": xfce_startup_script,
    },
}

loop_control = True

while loop_control:
    print("Possible configurations:")

    for name, config in configs.items():
        print(" " * 4, f"{config['number']}. {name}")

    choice = input("\n"+"Pick number to choose configuration: "+"\n")

    if choice not in (str(config["number"]) for config in configs.values()):
        print("\nWrong input! Try again!\n")
    else:
        loop_control = False

for name, config in configs.items():
    if int(choice) == config["number"]:

        home = Path(os.environ["HOME"])

        vnc_config_path = home.joinpath(".vnc/xstartup")

        # Create startup script
        with open(vnc_config_path, "w") as conf:
            conf.write(config["startup_script"])

        # Set up read + execution for startup script
        os.chmod(vnc_config_path, 0o555)


if vnc_config_path.exists():
    print("Startup script created succesfully")
else:
    print("Startup script creation failed")
