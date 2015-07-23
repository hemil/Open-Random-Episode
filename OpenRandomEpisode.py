'''
For Videos which you have seen over and over again.
Now, you just want to open any one and enjoy it.
like Friends.
Selects a Random Episode and starts to play it.

Hemil Shah

'''

import os
import random
import sys
from Tkinter import Tk
from tkFileDialog import askdirectory

'''
For TV shows which can be seen over and over again.
Selects a Random Episode and starts to play it.

Hemil Shah
'''

import os
import random
import sys
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory() # show an "Open" dialog box and return the path to the selected file
root = filename

li = []
for path, subdirs, files in os.walk(root):
    for name in files:
    	if name.lower().endswith(('.mp4','.avi','.mkv','.wmv','.m4v','.flv')):	
        	a = os.path.join(path, name)
        	li.append(a)

def choose_random(li):
	return random.choice(li)

print "Number of files: ",str(len(li))
rand_epi = choose_random(li)

print "Starting...." + rand_epi.split("\\")[3]
os.startfile(rand_epi, 'open')
print "It should have started"
