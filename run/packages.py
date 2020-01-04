# This module uses APT package manager.

import subprocess as s
packages = []

class apt:
  def update():
    try:
      s.call(["sudo apt update -y"], shell=False)
    except:
      print("There was an issue updating apt. Try again manually.")
