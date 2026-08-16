%global commit f051a09ade09b918c63e1fcf06663a022470b24a
%global soc     sc7280
Name:           alsa-ucm-conf-qcom-%{soc}
Version:        1
Release:        2%{?dist}
Summary:        ALSA UCM configuration for %{soc} devices
License:        BSD-3-Clause
URL:            https://github.com/sc7280-mainline/alsa-ucm-conf
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
