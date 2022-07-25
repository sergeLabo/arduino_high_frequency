from time import time, sleep
import pigpio

pi = pigpio.pi()

h = pi.spi_open(0, 40000)

# # stop = time() + 20
# # while time() < stop:

pi.spi_xfer(h, "5")

for i, item in enumerate("Hello, world!5"): 
	c, d = pi.spi_xfer(h, item)
	print("Send", i, item, "len", c, "val", d)
	sleep(1)

pi.spi_close(h)

pi.stop()
