import glob
import subprocess

import toml

fontconfig = {
    "family": "Twemoji Color Emoji",
    "color_format": "cff_colr_0",
    "version_major": "1",
    "version_minor": "2",
    "output_file": "TwemojiCOLR0.otf",
    # "clipbox_quantization": 32,
    # "clip_to_viewbox": False,
    # "clipbox_quantization": False,
    "master": {
        "regular": {
            "style_name": "Regular",
            "srcs": [i.replace("\\", "/") for i in glob.glob("./twemoji/assets/svg/*")],
            "position": {
                "wght": 400
            }
        }
    },
    "axis": {
        "wght": {
            "name": "Weight",
            "default": 400
        }
    }
}
with open("config.toml", "w+") as f:
    toml.dump(fontconfig, f)
proc = subprocess.run(["nanoemoji", "config.toml"])

# the following code fixes the font overriding the characters #*0123456789 but breaks their corresponding keykap emojis.

# if proc.returncode == 0:
#     print("Fixing cmap...")
#     # nanoemoji generates erroneous characters for the numbers, this removes them
#     font = TTFont("build/TwemojiCOLR0.otf")
#     for i in range(len(font["cmap"].tables)):
#         keys = list(font["cmap"].tables[i].cmap.keys())
#         for k in keys:
#             if k < 100:
#                 del font["cmap"].tables[i].cmap[k]
#
#     font.save("build/TwemojiCOLR0.otf")
