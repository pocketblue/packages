%global _commit 06a1b66670bade6959eac9af84358aba7f65f9f2

Name:      alsa-ucm-conf-sm7150
Version:   1.0
Release:   2
Summary:   ALSA UCM configuration for SM7150 devices
URL:       https://github.com/sm7150-mainline/alsa-ucm-conf
License:   BSD-3-Clause
BuildArch: noarch

Source1:   %{url}/archive/%{_commit}.tar.gz
Source2:   configs.files

Requires:  alsa-ucm

%description
%{summary}

%prep
tar -xzf %{SOURCE1}

%install
cd alsa-ucm-conf-%{_commit}
while IFS= read -r firmware; do
	install -Dm644 "${firmware}" "%{buildroot}/usr/share/alsa/${firmware}"
done < %{SOURCE2}

%files
/usr/share/alsa/*
