import praw,requests,re
import urllib.request
import PySimpleGUI as sg      
import os
from tkinter import filedialog
from tkinter import *


##########################GUI####################

layout = [[sg.Text('Please enter name of subreddit')],      
                 [sg.InputText()],
                 [sg.Text('Path')],
                 [sg.In(size=(25,1), enable_events = True, key="-FOLDER-"), 
                 sg.FolderBrowse()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('RedditImageDownloader', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    


##################SCRIPT######################
reddit = praw.Reddit(
    client_id="0-L0kz-b0jZ3Zw",
    client_secret="RLJy4IHTrGMPmuBANt56HPCztyhQEw",
    username="Western_Animator_605",
    password="BC5Drjr4E2XBNZ",
    user_agent="web:1001-1 by(u/Western_Animator_605")


subreddit = reddit.subreddit(text_input)

top = subreddit.top(limit = None)
count = 0
path = values["-FOLDER-"]
for submission in top:
    url = str(submission.url)
    filepath = os.path.join("/home/utsav/Desktop/",f"image{count}")
    # Check if the link is an image
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

        # Retrieve the image and save it in current folder
        urllib.request.urlretrieve(url, filepath)
        count += 1

        # Stop once you have 10 images
        if count == 1:
            break