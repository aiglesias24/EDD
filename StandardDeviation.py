from time import sleep
import statistics
stdev = []
counter = 1
counters = []
counters.append(counter)
sleep(.5)

while True:

    counters.append(counter)
    sleep(.5)
    stdev.append(statistics.stdev(counters))
    counter += 1