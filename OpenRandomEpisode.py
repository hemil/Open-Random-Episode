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


root = "Z:\\Theatre"
li = []
for path, subdirs, files in os.walk(root):
    for name in files:
        a = os.path.join(path, name)
        li.append(a)

def choose_random(li):
	return random.choice(li)

print "Number of files: ",str(len(li))
rand_epi = "-1"
#If it's not a video.
#Only open avi and mp4 files
while True:
	rand_epi = choose_random(li)
	temp = rand_epi.split("\\")
	file_name = temp[len(temp) - 1]

	#is a video? check extention
	if rand_epi.lower().endswith(('.mp4','.avi','.mkv','.wmv','.m4v','.flv','.vob','.ogv','.mov','.mpeg','.mpg')):	
		print "\nFile is a video"
		print "Starting....",file_name
		break
	else:
		print file_name," is NOT a video. Choosing Again..."
		continue
os.startfile(rand_epi, 'open')
print "should have started"
