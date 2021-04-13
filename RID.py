import praw
import requests
import re
import urllib.request
import PySimpleGUI as sg
import os
from tkinter import filedialog
from tkinter import *


##########################GUI####################
sg.theme('dark grey 9')
layout = [[sg.Text('Please enter name of subreddit')],
          [sg.InputText()],
          [sg.Text('Download Limit (max 100)')],
          [sg.In()],
          [sg.Text('Path'),
           sg.In(size=(25, 1), enable_events=False, key="-FOLDER-"),
           sg.FolderBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('RedditImageDownloader', layout)


event, values = window.read()
window.close()

text_input = values[0]
size = values[1]

##################SCRIPT######################
reddit = praw.Reddit(
    client_id="0-L0kz-b0jZ3Zw",
    client_secret="RLJy4IHTrGMPmuBANt56HPCztyhQEw",
    user_agent="linux:img_scraper:v0.1 (u/western_animator_605')")


subreddit = reddit.subreddit(text_input)
print(size)
top = subreddit.top(limit=5)
count = 0
path = values["-FOLDER-"]
while True:
    for submission in top:
        url = str(submission.url)
        filepath = os.path.join(path, f"image{count}")
        # Check if the link is an image
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

            # Retrieve the image and save it in current folder
            urllib.request.urlretrieve(url, filepath)
            count += 1

            # Stop once you have input size of images
            if count == size:
                break

