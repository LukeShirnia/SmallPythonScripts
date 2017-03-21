#!/usr/bin/python

import time
import datetime

now = datetime.datetime.now()
now_time = now.strftime('%b %d %H:%M')
now_mins_10 = now - datetime.timedelta(minutes = 10)
now_mins_10 = now_mins_10.strftime('%b %d %H:%M')
now_mins_80 = now - datetime.timedelta(minutes = 80)
now_mins_80 = now_mins_80.strftime('%b %d %H:%M')

print "Current time            %s" % (now_time)
print "Minus 10:               %s" % (now_mins_10)
print "Minus 1 hour 20 mins    %s" % (now_mins_80)