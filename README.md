# progress-bar
Progress bar for Python 3+

This is a script to create a generic progress bar. It requires no extra libraries. Feel free to tweak the script to fit what you are doing!

The user is able to customize the progress object, number of objects, and the "ticks" for each object.

==================================================

Use case:

`progressBar(countPerObject, totalNumberObject, waitTime, object[Optional])`

==================================================

`progressBar(5,20,0.05,"*")`:

The progress bar will be constructed using `"*"`, with 20 `"*"` on the progress bar, and each `"*"` takes 5 ticks (i.e. 5% of 100%). The waitTime will be the time in between each "tick"

https://i.imgur.com/SA0YZhi.png

==================================================

`progressBar(1,50,0.04)`:

Since there is no object defined, the default object `"█"` would be used. This progress bar will only go up to 50

https://i.imgur.com/dqYeCKY.png

==================================================

`progressBar(10,10,0.02,"foo bar")`:

In the case of the object being more than 1 character long, the script will only use the 1st character defined in object, in this case it is `"f"`

https://i.imgur.com/PZdcQH6.png
