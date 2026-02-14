%global armbian_build_commit 6f022174747f14f1b022f0eb707ff35cf1f5133c
%global shortcommit %(c=%{armbian_build_commit}; echo ${c:0:7})

Name:           armbian-led-state
Version:        1.0
Release:        1.git%{shortcommit}%{?dist}
Summary:        Armbian LED state save/restore service for Orange Pi 3 LTS
License:        GPL-2.0-only
URL:            https://github.com/armbian/build
Source0:        %{url}/raw/%{armbian_build_commit}/packages/bsp/common/usr/lib/armbian/armbian-led-state-restore.sh
Source1:        %{url}/raw/%{armbian_build_commit}/packages/bsp/common/usr/lib/armbian/armbian-led-state-save.sh
Source2:        %{url}/raw/%{armbian_build_commit}/packages/bsp/common/lib/systemd/system/armbian-led-state.service
Source3:        armbian-leds.conf
BuildArch:      noarch
AutoReqProv:    no

%description
Armbian LED state save/restore service and Orange Pi 3 LTS LED defaults.

%install
install -Dm 0755 %{SOURCE0} %{buildroot}/usr/lib/armbian/armbian-led-state-restore.sh
install -Dm 0755 %{SOURCE1} %{buildroot}/usr/lib/armbian/armbian-led-state-save.sh
install -Dm 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/armbian-led-state.service
install -Dm 0644 %{SOURCE3} %{buildroot}/etc/armbian-leds.conf

%files
/usr/lib/armbian/armbian-led-state-restore.sh
/usr/lib/armbian/armbian-led-state-save.sh
/usr/lib/systemd/system/armbian-led-state.service
/etc/armbian-leds.conf

%changelog
%autochangelog
