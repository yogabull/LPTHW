from datetime import datetime #first datetime is the module. The second is a submodule with the same name.
from time import sleep
from random import randint

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for num in range(5):
    delay = randint(1, 5)
    print(delay, "seconds")
    sleep(delay)
    right_this_minute = datetime.today().minute #this invokes method 'today' from submodule datetime
    if right_this_minute in odds:
        print("This minute seems to be a little odd.")
    else:
        print("Not an odd minute")
    #
#
# from os import getcwd
#
# where_am_I = getcwd()
# print(where_am_I)
#
# # or use this code
#
# import os #Importing module
# os.getcwd() #invoking funtionality (get current working directory)
#
# os.environ #using the 'environ' attribute produces a lot of data
# os.getenv('HOME') #function (getenv) to get the individual HOME data
#
#
# # date time module
# import datetime
# datetime.date.today()
# datetime.date.today() .day #returns day
# datetime.date.today() .month #returns month
# datetime.date.isoformat(datetime.date.today())
#
# # time module
# import time
# time.strftime('%H:%M') #This prints out current time in 24-hour format.
# time.strftime('%A %p') #gives day, am or pm
#
# #HTML escaping html tags
# import html
# html.escape("This HTML fragment contains a <script>script</script> tag.")
#
# html.unescape("I &hearts; Python's &lt; standard libary &gt;.")
