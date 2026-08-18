Name: alsa-ucm-conf-sm8250
Version: 1.1
Release: 1
Summary: alsa
Source1: Xiaomi Pad 6.conf
Source2: HiFi_pipa.conf
Source3: HDMI_pipa.conf
License: Unknown
BuildArch: noarch

Requires: alsa-ucm

%description
ALSA Use Case Manager configuration settings for sm8250-based devices.

%install
install -Dm644 "%{SOURCE1}" "%{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8250/Xiaomi Pad 6.conf"
install -Dm644 "%{SOURCE2}" "%{buildroot}%{_datadir}/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf"
install -Dm644 "%{SOURCE3}" "%{buildroot}%{_datadir}/alsa/ucm2/Qualcomm/sm8250/HDMI_pipa.conf"

ln -s "Xiaomi Pad 6.conf" "%{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8250/Xiaomi-Pad6-pipa-M82.conf"
ln -s "Xiaomi Pad 6.conf" "%{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8250/xiaomi-XiaomiPad6-.conf"

%files
%{_datadir}/alsa/ucm2/conf.d/sm8250/Xiaomi\ Pad\ 6.conf
%{_datadir}/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf
%{_datadir}/alsa/ucm2/Qualcomm/sm8250/HDMI_pipa.conf
%{_datadir}/alsa/ucm2/conf.d/sm8250/Xiaomi-Pad6-pipa-M82.conf
%{_datadir}/alsa/ucm2/conf.d/sm8250/xiaomi-XiaomiPad6-.conf

%changelog
%autochangelog
