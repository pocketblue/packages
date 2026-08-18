Name: pipa-sound-conf
Version: 2.1
Release: 1%{?dist}
Summary: Sound settings for Xiaomi Mi Pad 6 (pipa)
Source1: 51-pipa.conf
License: Unknown
BuildArch: noarch
Provides: alsa-ucm-conf-xiaomi-pipa = %{version}-%{release}
Obsoletes: alsa-ucm-conf-xiaomi-pipa < %{version}-%{release}

Requires: alsa-ucm-conf-sm8250
Requires: wireplumber

%description
Wireplumber configuration for Xiaomi Mi Pad 6 (pipa)

%install
install -Dm644 "%{SOURCE1}" "%{buildroot}%{_datadir}/wireplumber/wireplumber.conf.d/51-pipa.conf"

%files
%{_datadir}/wireplumber/wireplumber.conf.d/51-pipa.conf
