#!/usr/bin/env bash
set -euo pipefail

image="/usr/lib/u-boot/orangepi3-lts/u-boot-sunxi-with-spl.bin"

root_src="$(findmnt -nro SOURCE --target /sysroot --evaluate)"
root_dev="${root_src%%[*}"
parent="$(lsblk -nro PKNAME "$root_dev" | head -n1)"

disk="/dev/$parent"

if [ -z "$device" ] || [ ! -b "$device" ]; then
    echo "Block device not found: $device" >&2
    exit 1
fi

if [ ! -f "$image" ]; then
    echo "U-Boot image not found: $image" >&2
    exit 1
fi

if [ "$(id -u)" -ne 0 ]; then
    echo "Run as root to install U-Boot" >&2
    exit 1
fi

start_lba=16
ss=512 # Hardware sector size
start_bytes=$(( start_lba * ss ))

dd if="$uboot_bin" of=$disk oflag=seek_bytes bs=4K seek="$start_bytes" conv=notrunc,fsync status=progress
