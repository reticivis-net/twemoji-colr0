## generates a [COLR0](https://learn.microsoft.com/en-us/typography/opentype/spec/colr) font from [Twitter's Twemoji](https://github.com/twitter/twemoji) using [nanoemoji](https://github.com/googlefonts/nanoemoji) and [fonttools](https://github.com/fonttools/fonttools)

### requirements

- doesn't work on windows (nanoemoji requires every svg file to be passed as a path which is too long for windows)
- twemoji (submoduled here)
- nanoemoji/fonttools (install requirements in poetry.lock with [poetry](https://python-poetry.org/))

### usage

run the [main.py](main.py) file
