## generates a [COLR0](https://learn.microsoft.com/en-us/typography/opentype/spec/colr) font from [Twitter's Twemoji](https://github.com/twitter/twemoji) using [nanoemoji](https://github.com/googlefonts/nanoemoji) and [fonttools](https://github.com/fonttools/fonttools)

### requirements

- [twemoji](https://github.com/twitter/twemoji) (submoduled here)
- [nanoemoji](https://github.com/googlefonts/nanoemoji)/[fonttools](https://github.com/fonttools/fonttools) (install
  requirements in [poetry.lock](poetry.lock) with [poetry](https://python-poetry.org/))

### usage

- run the [main.py](main.py) file
- the final font file will be at `build/TwemojiCOLR0.otf`

### note

for [technical reasons](https://github.com/googlefonts/nanoemoji/issues/436#issuecomment-1256468336), the font generates
blank glyphs for the characters `#*1234567890`. uncomment the code at the bottom of [main.py](main.py) to fix this
behavior, [at the cost of breaking the "keycap" emojis](https://github.com/googlefonts/nanoemoji/issues/436#issuecomment-1256540076)