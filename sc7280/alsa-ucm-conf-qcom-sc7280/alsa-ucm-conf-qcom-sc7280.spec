%global commit 9d5563e6456e1a35e2d59c59130c50b2bbfe3c94
%global soc     sc7280
Name:           alsa-ucm-conf-qcom-%{soc}
Version:        1
Release:        3%{?dist}
Summary:        ALSA UCM configuration for %{soc} devices
License:        BSD-3-Clause
URL:            https://github.com/sc7280-mainline/alsa-ucm-conf
Source0:        %{url}/archive/%{commit}.tar.gz
BuildArch:      noarch

Provides:       alsa-ucm = 1.2.15.3-1
Conflicts:      alsa-ucm <= 1.2.15.3-1

%description
ALSA UCM configuration for %{soc} devices

%prep
%autosetup -n alsa-ucm-conf-%{commit}

%install
mkdir -p   %{buildroot}/usr/share/alsa
cp -r ucm2 %{buildroot}/usr/share/alsa

%files
/usr/share/alsa/ucm2

%changelog
%autochangelog
