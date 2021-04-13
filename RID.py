import praw,requests,re
import urllib.request

from PIL import Image

reddit = praw.Reddit(
    client_id="0-L0kz-b0jZ3Zw",
    client_secret="RLJy4IHTrGMPmuBANt56HPCztyhQEw",
    username="Western_Animator_605",
    password="BC5Drjr4E2XBNZ",
    user_agent="web:1001-1 by(u/Western_Animator_605")


subreddit = reddit.subreddit('earthporn')

top = subreddit.top(limit = None)
count = 0

for submission in top:
    url = str(submission.url)

    # Check if the link is an image
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

        # Retrieve the image and save it in current folder
        urllib.request.urlretrieve(url, f"image{count}")
        count += 1

        # Stop once you have 10 images
        if count == 10:
            break



