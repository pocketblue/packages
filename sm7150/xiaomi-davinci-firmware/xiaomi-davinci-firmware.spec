%global _commit 6532694920dd05ee7d930fe6d3ede74d2b9ea60d
%global __requires_exclude ^.*\\.so.*$

Name:           xiaomi-davinci-firmware
Version:        1.0
Release:        1
Summary:        Firmware for Xiaomi Mi 9T / Redmi K20
URL:            https://github.com/sm7150-mainline/firmware-xiaomi-davinci
Source0:        %{url}/archive/%{_commit}.tar.gz
Source1:        module-setup.sh
License:        Unfree

Requires:       dracut

%description
%{summary}

%prep
tar -xzf %{SOURCE0}

%install
install -Dm755 %{SOURCE1} %{buildroot}/usr/lib/dracut/modules.d/90-%{name}/module-setup.sh

cd firmware-xiaomi-davinci-%{_commit}
find . -type f -exec install -Dm644 {} "%{buildroot}"/{} \;

%files
/usr/lib/dracut/modules.d/90-%{name}/module-setup.sh
/usr/share/qcom/*
/lib/firmware/*
