import sys, time
def loading():
    print('Loading...')
    for i in range(0, 100):
        time.sleep(.02)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
