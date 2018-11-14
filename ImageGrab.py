import urllib
from urllib import (request)
import praw
import os
import sys


class ImageGrab:

    def ImageGrab(self, foo):
        foo = False

    def GetMeme(self):
        print("Hello, world!")

        # create a read only instance of reddit
        reddit = praw.Reddit(client_id="My client id", client_secret="my client secret", user_agent="my user agent")
        meme_hub = reddit.subreddit('dankmemes')  # open the subreddit

        doot = meme_hub.top(1)  # get the post
        doot_url = doot.url  # get the url

        filepath = os.getcwd()  # what folders are we in?

        viewer = urllib.urlopen(page_link) # opens up r/dankmemes top post

        for visuals in viewer.findall("img"):  # comb through the images on the page
            if visuals.endswith(".png"):  # if there's a png file
                urlretrieve(visuals, filepath)  # get it and save it in the system
            else:
                print("failed to retrieve\n")  # debug error print


# main()
