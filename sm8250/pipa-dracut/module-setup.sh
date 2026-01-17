#!/usr/bin/bash

# called by dracut
install() {
    inst "/usr/lib/firmware/novatek/nt36532_csot.bin"
    inst "/usr/lib/firmware/novatek/nt36532_tianma.bin"
}
