
# EPM11-MCU


Example project for the MCU component of the [EPM11](https://brisbanesilicon.com.au/epm11) MCU-FPGA development board by [BrisbaneSilicon](https://brisbanesilicon.com.au/).
<br><br>

## Table of Contents

*   [Overview](#overview)
*   [Getting Started](#getting-started)


## Overview

This project allows the user to build an custom Micropython layer for MCU-FPGA communications and upload it onto the [EPM11](https://brisbanesilicon.com.au/epm11) MCU-FPGA development board. Alternatively, a pre-built version of the module is hosted in the '[bin](https://github.com/BrisbaneSilicon/EPM11-MCU/tree/master/bin)' for users that simply want to upload and utilise it.

This project also contains the currently supported Micropython image, a [pin-mapping script](https://github.com/BrisbaneSilicon/EPM11-MCU/blob/master/script/pinout.py), as well as various example scripts.

The core component of this project (together with its [EPM11-FPGA](https://github.com/BrisbaneSilicon/EPM11-FPGA) sister project) is the MCU-FPGA comms layer. This layer can be leveraged by the user for 'out of the box' MCU-FPGA communication, upon which their custom functionality can be developed.


![MCU FPGA Comms](img/mcu_fpga_comms.png)


After the comms layer of this project has been built and uploaded, and its [EPM11-FPGA](https://github.com/BrisbaneSilicon/EPM11-FPGA) sister project flashed to the FPGA, communication between the two IC's is as simple as:

#### MCU

On the RP2350 MCU, via a Python program or REPL:

```python
import fpga

fpga.write(0x4, 0xFF)
```

#### FPGA

The Python snippet above will produce a AXI-Lite (ish) write transaction, with wdata=0xFF and addr=0x4. This interface is plumbed to the user module '[user.sv](https://github.com/BrisbaneSilicon/EPM11-FPGA/blob/master/proj/common/systemverilog/user.sv)':

```systemverilog
output  reg [31:0]  cpu_addr,
output  reg [31:0]  cpu_wdata,
output  reg [3:0]   cpu_wstrb,
input       [31:0]  cpu_rdata,
output  reg         cpu_valid,
input               cpu_ready
```

<br>

## Getting Started

Fulfill the below prerequisites.

### Prerequisites

1. A PC running an x64 compatible, Debian-based flavour of Linux or Windows 11.
   - Other flavours of Linux may work but aren't officially supported.
   - We recommend [Ubuntu](https://ubuntu.com/).
2. An installation of [GIT](https://git-scm.com/).
3. Either an installation of [Thonny](https://thonny.org/) or a command-line based tool for interacting with the RP2350 MCU, i.e. [mpremote](https://pypi.org/project/mpremote/).
4. A copy of this repository.
   - Launch a terminal program.
   - Navigate to the directory in which you wish to host the EPM11 repository.
   - `git clone https://github.com/BrisbaneSilicon/EPM11-MCU.git`
  
If you wish to build the custom Micropython layer:

1. A copy of Micropython (located in the same root directory as this repository)
  - Launch a terminal program.
  - Navigate to the same directory in which you host the EPM11 repository.
  - `git clone https://github.com/BrisbaneSilicon/EPM11-MCU.git`
2. An installation of version 13.3.rel1 of the Arm cross compiler toolchain. See [here](https://github.com/RT-Thread/toolchains-ci/releases).
3. An installation of Python3.
4. An installation of the Python library pyelftools (`pip install 'pyelftools>=0.25'`)
