import time
import random

def waiting_game():
    
    goal_time = random.randint(1, 5)
    print(f"Your target time is {goal_time} seconds.")
    
    input("---Press Enter to Begin---")
    start_time = time.time()

    input(f"Press Enter again after {goal_time} seconds.")
    end_time = time.time()
    tot_time = round(end_time - start_time,3)

    print(f"Your time: {tot_time :.3f} seconds.")
    if tot_time == goal_time:
        print("Good job!")
    elif tot_time < goal_time:
        print(f"You were {goal_time - tot_time :.3f} seconds too fast.")
    else:
        print(f"You were {tot_time - goal_time :.3f} seconds too slow.")

waiting_game()