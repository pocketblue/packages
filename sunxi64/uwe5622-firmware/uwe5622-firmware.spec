%global commit db5e86200ae592c467c4cfa50ec0c66cbc40b158
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           uwe5622-firmware
Version:        1.0
Release:        7.git%{shortcommit}%{?dist}
Summary:        Unisoc UWE5622 (AW859A) Wi-Fi/Bluetooth firmware
License:        Unknown
URL:            https://github.com/orangepi-xunlong/firmware
Source0:        %{url}/archive/%{commit}/firmware-%{commit}.tar.gz
Source1:        aw859a-wifi.service
Source2:        sprd-bluetooth
Source3:        sprd-bluetooth.service
Source4:        uwe5622-wireless.conf
Source5:        aw859a-bluetooth.service
BuildArch:      noarch
AutoReqProv:    no
Requires:       hciattach-opi

%description
Firmware for the Unisoc UWE5622 (AW859A) Wi-Fi/Bluetooth combo.
Packaged from the Orange Pi firmware repository.

%prep
%autosetup -n firmware-%{commit}

%install
install -Dm 0644 wcnmodem.bin %{buildroot}/usr/lib/firmware/uwe5622/wcnmodem.bin
install -Dm 0644 wifi_2355b001_1ant.ini %{buildroot}/usr/lib/firmware/uwe5622/wifi_2355b001_1ant.ini
install -Dm 0644 bt_configure_rf.ini %{buildroot}/usr/lib/firmware/uwe5622/bt_configure_rf.ini
install -Dm 0644 bt_configure_pskey.ini %{buildroot}/usr/lib/firmware/uwe5622/bt_configure_pskey.ini
ln -s uwe5622/wcnmodem.bin %{buildroot}/usr/lib/firmware/wcnmodem.bin
ln -s uwe5622/wifi_2355b001_1ant.ini %{buildroot}/usr/lib/firmware/wifi_2355b001_1ant.ini
install -Dm 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/aw859a-wifi.service
install -Dm 0755 %{SOURCE2} %{buildroot}/%{_bindir}/sprd-bluetooth
install -Dm 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/sprd-bluetooth.service
install -Dm 0644 %{SOURCE4} %{buildroot}/usr/lib/modules-load.d/uwe5622-wireless.conf
install -Dm 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/aw859a-bluetooth.service

%files
/usr/lib/firmware/uwe5622/wcnmodem.bin
/usr/lib/firmware/uwe5622/wifi_2355b001_1ant.ini
/usr/lib/firmware/uwe5622/bt_configure_pskey.ini
/usr/lib/firmware/uwe5622/bt_configure_rf.ini
/usr/lib/firmware/wcnmodem.bin
/usr/lib/firmware/wifi_2355b001_1ant.ini
/usr/lib/systemd/system/aw859a-wifi.service
/usr/lib/systemd/system/aw859a-bluetooth.service
/usr/lib/systemd/system/sprd-bluetooth.service
/usr/lib/modules-load.d/uwe5622-wireless.conf
%{_bindir}/sprd-bluetooth

%changelog
%autochangelog
