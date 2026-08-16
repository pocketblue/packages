%global commit f051a09ade09b918c63e1fcf06663a022470b24a
%global soc     sc7280
Name:           alsa-ucm-conf-qcom-%{soc}
Version:        1
Release:        3%{?dist}
Summary:        ALSA UCM configuration for %{soc} devices
License:        BSD-3-Clause
URL:            https://github.com/sc7280-mainline/alsa-ucm-conf
Source0:        %{url}/archive/%{commit}.tar.gz
BuildArch:      noarch
Requires:       alsa-ucm

%description
ALSA UCM configuration for %{soc} devices that upstream alsa-ucm-conf does
not carry yet. The shared parts of the configuration tree - codec sequences,
libraries and common includes - come from alsa-ucm.

%prep
%autosetup -n alsa-ucm-conf-%{commit}

%install
install -d %{buildroot}%{_datadir}/alsa/ucm2

# Only install the device configuration. This fork tracks an older
# alsa-ucm-conf, so shipping its whole ucm2 tree would both conflict with
# alsa-ucm and replace the rest of the tree with stale copies.
cp -a ucm2/Fairphone ucm2/Nothing %{buildroot}%{_datadir}/alsa/ucm2/

install -D -p -m 0644 "ucm2/conf.d/qcm6490/Fairphone 5.conf" \
    "%{buildroot}%{_datadir}/alsa/ucm2/conf.d/qcm6490/Fairphone 5.conf"
install -D -p -m 0644 ucm2/conf.d/sm8250/NP1.conf \
    %{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8250/NP1.conf

%files
%license LICENSE
%{_datadir}/alsa/ucm2/Fairphone
%{_datadir}/alsa/ucm2/Nothing
"%{_datadir}/alsa/ucm2/conf.d/qcm6490/Fairphone 5.conf"
%{_datadir}/alsa/ucm2/conf.d/sm8250/NP1.conf

%changelog
%autochangelog
