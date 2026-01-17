Name: pipa-sensors
Version: 1.2
Release: 1
Summary: Sensors configs for the Xiaomi Pad 6
Source1: 81-libssc-xiaomi-pipa.rules
Source2: hexagonrpcd-sdsp.conf
License: MIT

Requires: xiaomi-pipa-firmware
Requires: iio-sensor-proxy
Requires: hexagonrpc

%description
Sensors configs for the Xiaomi Pad 6

%install
install -Dm644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d/81-libssc-xiaomi-pipa.rules
install -Dm644 %{SOURCE2} %{buildroot}/usr/share/hexagonrpcd/hexagonrpcd-sdsp.conf

%files
/usr/lib/udev/rules.d/81-libssc-xiaomi-pipa.rules
/usr/share/hexagonrpcd/hexagonrpcd-sdsp.conf
