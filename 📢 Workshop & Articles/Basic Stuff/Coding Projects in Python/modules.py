'''
Some popular python modules is
*) webbrowser
*) socket
*) random
*) statistics
*) datetime
'''

import webbrowser
from time import time as time_now
from random import choice
direction = choice(['N', 'S', "E", "W"])
print(direction)

# current time
now = ((time_now() // 60) // 60) // 24
print(now)

# webbrowser
webbrowser.open_new_tab(url='https://facebook.com')
