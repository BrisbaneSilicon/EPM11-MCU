# NOTE: the FPGA firmware that is compatible with this module
# is built with the '-t / --bus_test' command line argument

import fpga

# The four addresses the FPGA decodes.
ADDRESSES = (0x00000000, 0x000000FC, 0x5A5AA5A4, 0xFFFFFFFC)

# Between them these drive every data bit both high and low.
VALUES = (0xFFFFFFFF, 0xAAAAAAAA, 0x55555555, 0x0000FFFF, 0xFFFF0000, 0x8badf00d, 0x01234567, 0x00000000)

failures = 0
total = len(ADDRESSES) * len(VALUES)

print("\n\t------- Begin: EPM11 FPGA Bus Test -------\n")

print("|    Address   |     Write    |      Read    | Result |")
print("|--------------|--------------|--------------|--------|")
for address in ADDRESSES:
    for value in VALUES:
        fpga.write(address, value)
        val = fpga.read(address)

        if val == value:
            result = "PASS"
        else:
            result = "FAIL"
            failures += 1

        print("|  0x{:08X}  |  0x{:08X}  |  0x{:08X}  |  {}  |".format(
            address, value, val, result))


print("\nSummary: {} of {} tests failed".format(failures, total))
