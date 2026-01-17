Name:           xiaomi-nabu-configs
Version:        1
Release:        0%{?dist}
Summary:        configs for xiaomi pad 5
License:        GPL-3.0-or-later
BuildArch:      noarch
Source1:        99-libinput-calibration-matrix.rules
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
%{summary}

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-libinput-calibration-matrix.rules
install -D -m 644 /dev/null %{buildroot}%{_prefix}/lib/device-rotate

%files
%{_udevrulesdir}/99-libinput-calibration-matrix.rules
%{_prefix}/lib/device-rotate

%changelog
%autochangelog
