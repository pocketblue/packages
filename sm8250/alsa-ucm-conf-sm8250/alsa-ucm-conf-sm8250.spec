Name: alsa-ucm-conf-sm8250
Version: 1.0
Release: 1
Summary: alsa
Source1: Xiaomi Pad 6.conf
Source2: HiFi_pipa.conf
License: Unknown
BuildArch: noarch

Requires: alsa-ucm

%description
ALSA Use Case Manager configuration settings for sm8250-based devices.

%install
install -Dm644 "%{SOURCE1}" "%{buildroot}/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi Pad 6.conf"
install -Dm644 "%{SOURCE2}" "%{buildroot}/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf"

%files
/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf
/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi\ Pad\ 6.conf
