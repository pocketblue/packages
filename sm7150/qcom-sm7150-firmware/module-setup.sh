#!/usr/bin/bash

# called by dracut
install() {
  inst "/lib/firmware/qcom/a630_gmu.bin"
  inst "/lib/firmware/qcom/a630_sqe.fw"
}
