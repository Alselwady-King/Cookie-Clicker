import pathlib

CURRENT_DIR = pathlib.Path.cwd()  # Gets the current working directory, so where the program is being run from.

# Then, whereever your cookie folder is
IMAGE_DIR = CURRENT_DIR / "backgrounds"
TEXT_DIR = CURRENT_DIR / "Fonts"

# Cookie
COOKIE_PATH = IMAGE_DIR / "cookieImage.png"
# Cursive path
CURSIVE_PATH = TEXT_DIR / "Quetine.ttf"

