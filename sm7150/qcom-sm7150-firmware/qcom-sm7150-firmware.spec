Name: qcom-sm7150-firmware
Version: 1.0
Release: 2
Summary: Firmware package for SM7150 platform
Source1: module-setup.sh
License: Unfree

Requires: qcom-firmware
Requires: qcom-sm7150-atheros-firmware
Requires: xiaomi-davinci-firmware
Requires: dracut

%description
%{summary}

%install
install -Dm755 %{SOURCE1} %{buildroot}/usr/lib/dracut/modules.d/90qcomfw/module-setup.sh

%files
/usr/lib/dracut/modules.d/90qcomfw/*
