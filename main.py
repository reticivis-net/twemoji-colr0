import glob
import subprocess

from fontTools.ttLib import TTFont

proc = subprocess.run(["nanoemoji",
                       "--family", "Twemoji Color Emoji",
                       "--color_format", "cff_colr_0",
                       "--version_major", "1",
                       "--version_minor", "1",
                       "--output_file", "TwemojiCOLR0.otf",
                       # only works on linux due to length limit
                       *(glob.glob("./twemoji/assets/svg/*"))
                       ])

if proc.returncode == 0:
    print("Fixing cmap...")
    # nanoemoji generates erroneous characters for the numbers, this removes them
    font = TTFont("build/TwemojiCOLR0.otf")
    for i in range(len(font["cmap"].tables)):
        keys = list(font["cmap"].tables[i].cmap.keys())
        for k in keys:
            if k < 100:
                del font["cmap"].tables[i].cmap[k]

    font.save("TwemojiCOLR0.otf")
