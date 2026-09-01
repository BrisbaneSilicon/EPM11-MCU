# RP2350 I/O connector, J5:
j5 = {
    1   : { "type" : "GPIO",    "idx" : 25  },
    2   : { "type" : "ADC_VREF"             },
    3   : { "type" : "ADC",     "idx" : 29  },
    4   : { "type" : "ADC",     "idx" : 28  },
    5   : { "type" : "ADC",     "idx" : 27  },
    6   : { "type" : "ADC",     "idx" : 26  },
    7   : { "type" : "GPIO",    "idx" : 24  },
    8   : { "type" : "GPIO",    "idx" : 20  },
    9   : { "type" : "GPIO",    "idx" : 17  },
    10  : { "type" : "GPIO",    "idx" : 19  },
    11  : { "type" : "GPIO",    "idx" : 18  },
    12  : { "type" : "GPIO",    "idx" : 23  },
    13  : { "type" : "RUN"                  },
    14  : { "type" : "GPIO",    "idx" : 16  }
}

# RP2350 FPGA connections:
fpga_pins = {
    25  : { "idx" : 21   },
    26  : { "idx" : 22   },
    27  : { "idx" : 15   },
    28  : { "idx" : 14   },
    29  : { "idx" : 13   },
    30  : { "idx" : 12   },
    31  : { "idx" : 11   },
    32  : { "idx" : 10   },
    33  : { "idx" : 9    },
    34  : { "idx" : 8    },
    35  : { "idx" : 7    },
    36  : { "idx" : 6    },
    37  : { "idx" : 5    },
    38  : { "idx" : 4    },
    39  : { "idx" : 3    },
    40  : { "idx" : 2    },
    41  : { "idx" : 1    },
    42  : { "idx" : 0    }
}


# Demonstration
if __name__ == "__main__":
    import sys
    import select
    import time
    from machine import Pin, ADC

    poller = select.poll()
    poller.register(sys.stdin, select.POLLIN)

    print("------- EPM11 RP2350 I/O Demonstration -------")
    print("Begin per-PIN demo of RP2350 I/O bus, 'J5'.\n")
    print("NOTE: press <ENTER> to proceed to next PIN")
    print("      in demonstration.")
    print("----------------------------------------------")

    b = False
    for i in range(len(j5)):
        pin = 1 + i

        # NOTE: clear stdin
        if poller.poll(0):
            sys.stdin.readline()

        if j5[pin]["type"] == "GPIO":
            gpio = Pin(j5[pin]["idx"], Pin.OUT)
            while True:
                b = not b

                print(f"\rToggling PIN{pin} (GPIO): ", end="")
                if b:
                    print("HIGH\t", end="")
                    gpio.value(1)
                else:
                    print("LOW\t", end="")
                    gpio.value(0)

                time.sleep(1)

                if poller.poll(0):
                    sys.stdin.readline()
                    del pin
                    break

        elif j5[pin]["type"] == "ADC":
            adc = ADC(Pin(j5[pin]["idx"]))
            while True:
                voltage = 3.3 * (adc.read_u16() / 65535)

                print(f"\rVoltage PIN{pin} (ADC): {voltage:.2f}", end="")

                time.sleep(1)

                if poller.poll(0):
                    sys.stdin.readline()
                    del adc
                    break

        else:
            print(f"PIN{pin} is of non-demoable type '{j5[pin]["type"]}'")


    print("------- END Demonstration -------")

    for i in range(len(fpga_pins)):
        loc = 25 + i

        print(f"FPGA PIN of LOC={loc} is RP2350 Pin of index:{fpga_pins[loc]["idx"]}")