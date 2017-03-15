'''
For Videos which you have seen over and over again.
Now, you just want to open any one and enjoy it.
like Friends.
Selects a Random Episode and starts to play it.

Hemil Shah

'''

import os
import random
import subprocess
from Tkinter import Tk
import tkFileDialog

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askdirectory(initialdir='.')

li = []
for path, subdirs, files in os.walk(filename):
    for name in files:
        if name.lower().endswith(('.mp4', '.avi', '.mkv', '.wmv', '.m4v', '.flv')):
            a = os.path.join(path, name)
            li.append(a)


def choose_random(li):
    return random.choice(li)


print "Number of files: ", str(len(li))
rand_epi = choose_random(li)

subprocess.call(['open', rand_epi])
print "{file_name} should have started.".format(file_name=rand_epi.split("/")[-1])
