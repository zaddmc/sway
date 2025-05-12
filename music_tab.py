#!/usr/bin/python3
import subprocess
import json

workspaces = subprocess.run(
    ["swaymsg", "-t", "get_workspaces"], stdout=subprocess.PIPE
).stdout.decode("utf-8")
data = json.loads(workspaces)

for shit in data:
    if shit["num"] == 12 and shit["representation"] in ["H[]", None]:
        subprocess.run(["firefox", "--new-window", "https://music.youtube.com/"])
