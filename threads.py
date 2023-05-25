import threading
import time


start_time = time.perf_counter()


def dude_one():
    print("let me sleep for 3 seconds")
    time.sleep(3)
    print("Slept for 3 seconds")


def dude_two():
    print("let me sleep for 2 seconds")
    time.sleep(2)
    print("Slept for 2 Secs")


t1 = threading.Thread(target=dude_one)
t2 = threading.Thread(target=dude_two)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished {round(finish-start_time, 2)} seconds")
