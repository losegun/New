
# I don't know if there is already something similar out there but I now program for about a year and I didn't found any solution besides the two concepts (mp and sleep) to stop out different processes sometimes.

# My task in my actual project was to halt an particular process for 30 seconds without stopping the whole script. My programming skills are not on high level, so many guys of you for sure will perhaps find something to nag. Feel free to do it.

# The tricky part on that task was the "60 second border" which I managed good, I think. For time frames over 60 second it has to be tweaked. I didn't do this. Feel free to do it if you need it.

# Ok, long story short, here is my script.

from time import time
from time import strftime

minute_list = []
second_list = []
app_ping = 0

minute_bool = False
second_over_60 = False
second_under_60 = False


# Function to control the timer. In a you simply declare the time frame you need ( in seconds ).

def minute_man(a=30):
    global minute_bool, second_over_60, second_under_60
    global app_ping

    if len(second_list) >= 2:
        if (second_list[0] + a) > 60:
            if second_list[0] > a:
                rest = 60 - second_list[0]
                rest_2 = a - rest
                if minute_bool is True and second_list[-1] >= rest_2:
                    second_over_60 = True
                    minute_list.clear()
                    second_list.clear()
                    app_ping = 0
                    second_over_60 = False
                    minute_bool = False
        elif (second_list[0] + a) < 60:
            if second_list[-1] >= (second_list[0] + a):
                second_under_60 = True
                minute_list.clear()
                second_list.clear()
                app_ping = 0
                second_under_60 = False
                minute_bool = False
    if len(minute_list) >= 2:
        if minute_list[0] == 59 and minute_list[-1] == 0:
            minute_bool = True
        elif minute_list[0] < 59 and (minute_list[-1] == (minute_list[0] + 1)):
            minute_bool = True
        else:
            minute_bool = False

    # print(minute_bool, second_over_60, second_under_60)
    
# App which has to do something every 30 seconds:

def app():
    global app_ping

    current = strftime("%H:%M:%S")
    current_minute = strftime("%M")
    app_now = time()
    app_second = float(app_now % 60)

    if app_ping == 0:
        app_ping += 1
        minute_list.append(int(current_minute))
        second_list.append(app_second)
        print("done", "Time Stamp:", current)

# The loop. I chose float / milliseconds for the most possible accuracy.

while True:
    now = time()
    second = float(now % 60)
    minute_time = strftime("%M")

    minute_man()
    app()

    if app_ping > 0:
        minute_list.append(int(minute_time))
        second_list.append(second)

Output:

done Time Stamp: 21:15:33
done Time Stamp: 21:16:03
done Time Stamp: 21:16:33
