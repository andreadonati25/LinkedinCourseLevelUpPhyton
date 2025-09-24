import time
import sched

def plan_function(time_event, function, *args):
    schedule = sched.scheduler(time.time,time.sleep)
    schedule.enterabs(time_event,1,function,argument=args)
    print(f"{function.__name__} function scheduled for {time.asctime(time.localtime(time_event))}.")
    schedule.run()


plan_function(time.time() + 1, print, "Hello World")
plan_function(time.time() + 1, print, "Hello World", "Scheduled at", time.asctime(time.localtime(time.time())))