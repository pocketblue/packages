Name:           alsa-ucm-conf-sm8150
Version:        1
Release:        2
Summary:        alsa and pipewire audio profile for mipad5
License:        MIT
BuildArch:      noarch
Source0:        HiFi.conf
Source1:        sm8150.conf
Source2:        89-xiaomi_nabu.conf
Source3:        nabu.pa
Requires:       alsa-ucm

%description
%{summary}

%install
install -Dm644 "%{SOURCE1}" "%{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf"
install -Dm644 "%{SOURCE0}" "%{buildroot}%{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf"
install -Dm644 "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/pulse/daemon.conf.d/89-xiaomi_nabu.conf"
install -Dm644 "%{SOURCE3}" "%{buildroot}%{_sysconfdir}/pulse/default.pa.d/nabu.pa"

%files
%{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf
%{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/89-xiaomi_nabu.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa.d/nabu.pa

%changelog
%autochangelog
