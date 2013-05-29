import time

def run(bulb, delay=0):
    # Number of steps between min and max
    max_loop = 9

    # Main loop
    i = 0
    while i < max_loop:
        bulb.brightness_up()

        i += 1
        if i == max_loop:
            break

        time.sleep(delay)