
"""
#include <SPI.h>
#include "SPI_anything.h"

// create a structure to store the different data values:
typedef struct myStruct
{
  byte a;
  int b;
  long c;
};

myStruct foo;

void setup ()
  {
  SPI.begin ();
  // Slow down the master a bit
  SPI.setClockDivider(SPI_CLOCK_DIV8);

  foo.a = 42;
  foo.b = 32000;
  foo.c = 100000;
  }  // end of setup

void loop ()
  {
  digitalWrite(SS, LOW);    // SS is pin 10
  SPI_writeAnything (foo);
  digitalWrite(SS, HIGH);
  delay (1000);  // for testing

  foo.c++;
  }  // end of loop
"""


from time import time, sleep

import pigpio

pi = pigpio.pi()


HANDLE = pi.spi_open(0, 40000)
SS = 8  # Pin du SS sur la Pi

# Disable Slave Select
pi.write(SS, 1)
sleep(0.002)

pi.spi_xfer(HANDLE, "5")
sleep(0.0002)

for i, item in enumerate("Hello, world!5"):
    c, d = pi.spi_xfer(HANDLE, item)
    print("Send", i, item, "len", c, "val", d)
    sleep(1)

pi.spi_close(h)

pi.stop()
