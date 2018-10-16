import urllib
from urllib import (request)
import os
import sys

page_link = "https://www.reddit.com/r/dankmemes/top/"
meme_folder = "0_0" # folder for saving images


def main():
    print("Hello, world!")
    urllib.request.urlopen(page_link) # opens up r/dankmemes top page


main()
