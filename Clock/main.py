hour = int(input())
if hour >= 12:
    hour -= 12
minute = int(input())
mi = hour * 5
min = 0
mini = 0
ho = hour + 1
if mi > minute:
    min = mi - minute
    print(min)
else:
    mini = 60 - minute
    ho *= 5
    done = mini + ho
    print (done)

