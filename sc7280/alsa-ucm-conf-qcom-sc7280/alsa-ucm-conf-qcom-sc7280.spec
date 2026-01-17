%global commit e2f6767c294c458a2b02214d5c74460b1c50eed8
%global soc     sc7280
Name:           alsa-ucm-conf-qcom-%{soc}
Version:        1
Release:        0%{?dist}
Summary:        ALSA UCM configuration for %{soc} devices
License:        BSD-3-Clause
URL:            https://github.com/%{soc}-mainline/alsa-ucm-conf
Source0:        %{url}/archive/%{commit}.tar.gz
BuildArch:      noarch

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
