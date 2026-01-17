%global _firmwarepath /usr/lib/firmware
%global _hexegonpath /usr/share/qcom/sm8250/Xiaomi/pipa
%global _commit 842d35beffeda8c6d1b0e611b335543bf0e6b41e
%global __requires_exclude ^.*\\.so.*$

Name: xiaomi-pipa-firmware
Version: 1.1
Release: 2
URL: https://github.com/pipa-mainline/xiaomi-pipa-firmware
Summary: Firmware package for Xiaomi Pad 6 (pipa)
Source1: %{url}/archive/%{_commit}/xiaomi-pipa-firmware-%{_commit}.tar.gz
Source2: awinic_firmware.files
Source3: dsp_firmware.files
Source4: qcom_firmware.files
Source5: novatek_firmware.files
License: Unknown

Requires: qcom-firmware

%description
Firmware for various compoents in Xiaomi Mi Pad 6 including 
touchscreen, SoC.

%prep
tar -xzf %{SOURCE1}

%install
cd %{name}-%{_commit}

for firmware in $(cat %{SOURCE2}); do
	install -Dm644 ${firmware} "%{buildroot}/%{_firmwarepath}/awinic/$(basename "${firmware}")"
done

for firmware in $(cat %{SOURCE3}); do
	install -Dm644 ${firmware} "%{buildroot}/${firmware}"
done

for firmware in $(cat %{SOURCE4}); do
	install -Dm644 ${firmware} "%{buildroot}/%{_firmwarepath}/qcom/sm8250/xiaomi/pipa/$(basename "${firmware}")"
done

for firmware in $(cat %{SOURCE5}); do
	install -Dm644 ${firmware} "%{buildroot}/%{_firmwarepath}/novatek/$(basename "${firmware}")"
done

%files
%{_firmwarepath}/qcom/*
%{_firmwarepath}/novatek/*
%{_firmwarepath}/awinic/*
%{_hexegonpath}/*
