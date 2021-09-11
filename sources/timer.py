import time


def time_is(t_hour:int, t_min:int = 0):
    if t_hour > 24 or t_hour < 0:
        print("hour should be [0, 24]")
    if t_min > 60 or t_min < 0:
        print("minuite should be [0, 60]")

    while True:
        now = time.localtime()
        if now.tm_hour == t_hour and now.tm_min == t_min:
            print("now is the time!!")
            print(time.localtime())
            return True
        time.sleep(5)


if __name__ == "__main__":
    if time_is(22, 13):
        print("timer excuted!")
    print("rest of code")
