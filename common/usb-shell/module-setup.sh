#!/bin/bash

check() { return 0; }
depends() { echo dracut-systemd; }

install() {
  inst_multiple bash setsid stty sleep dmesg journalctl cat ls uname
  inst_script $moddir/usb-shell /usr/bin/usb-shell
  inst_simple $moddir/usb-shell.service $systemdsystemunitdir/usb-shell.service
  inst_simple $moddir/90-usb-shell-service.conf $systemdsystemunitdir/dracut-emergency.service.d/90-usb-shell.conf
  inst_simple $moddir/90-usb-shell-service.conf $systemdsystemunitdir/emergency.target.d/90-usb-shell.conf
}
