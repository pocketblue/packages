%global _commit 06a1b66670bade6959eac9af84358aba7f65f9f2

Name:      alsa-ucm-conf-sm7150
Version:   1.0
Release:   1
Summary:   ALSA UCM configuration for SM7150 devices
URL:       https://github.com/sm7150-mainline/alsa-ucm-conf
License:   BSD-3-Clause
BuildArch: noarch

Source1:   %{url}/archive/%{_commit}.tar.gz

Requires:  alsa-ucm

%description
%{summary}

%prep
tar -xzf %{SOURCE1}

%install
cd alsa-ucm-conf-%{_commit}
find ucm2 -type f -exec install -Dm644 {} %{buildroot}/usr/share/alsa/{} \;

%files
/usr/share/alsa/*
