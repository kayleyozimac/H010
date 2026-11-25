#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:40:51 2026

@author: kayleyozimac
"""

"""
make_stimulus_list.py
Writes stimuli/stimuli.js, the list of image files the H010 web task loads.
Run it (e.g. in Spyder) from the folder that holds index.html, every time you add,
remove, or rename images in stimuli/. Then commit stimuli/ (images + stimuli.js).

Uses the same rule as H010_setsize_CBE.py: every .png/.jpg/.jpeg in the folder, sorted by name.
"""
import os, json

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

STIM_DIR = os.path.join(BASE_DIR, "stimuli")
NEED = 2 * 48 + 2 * 4          # 96 trained (48 pairs) + 8 NC2 foils

files = sorted(f for f in os.listdir(STIM_DIR)
               if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.startswith("."))

with open(os.path.join(STIM_DIR, "stimuli.js"), "w", encoding="utf-8") as fh:
    fh.write("// Written by make_stimulus_list.py. Don't edit by hand; re-run the script instead.\n")
    fh.write("window.STIMULUS_FILES = " + json.dumps(files, indent=1) + ";\n")

print(f"Wrote stimuli/stimuli.js with {len(files)} images.")
if len(files) < NEED:
    print(f"WARNING: the task needs at least {NEED}. Add {NEED - len(files)} more.")