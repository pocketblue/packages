Name: pipa-sound-conf
Version: 1.4
Release: 1
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
install -Dm644 "%{SOURCE1}" "%{buildroot}/usr/share/wireplumber/wireplumber.conf.d/51-pipa.conf"

%files
/usr/share/wireplumber/wireplumber.conf.d/51-pipa.conf
