%global _ath10k_fw_commit 792c716c85c06861c4d17bce5ec21fba7f0f7de6
%global _linux_fw_commit  06a743fd69999590e88199bb9edba9d5b73d6ad1

Name: qcom-sm7150-atheros-firmware
Version: 20260110
Release: 2
URL: https://github.com/sm7150-mainline/firmware-qcom-sm7150-ath10k
Summary: Athernos firmware package for SM7150 platform
Source1: %{url}/archive/%{_ath10k_fw_commit}/ath10k-firmware.tar.gz
Source2: https://gitlab.com/kernel-firmware/linux-firmware/-/archive/%{_linux_fw_commit}/linux-firmware.tar.gz
License: Unfree

Provides: atheros-firmware = 20260110

BuildRequires: qca-swiss-army-knife, xz

%description
%{summary}

%prep
tar -xzf %{SOURCE1}
tar -xzf %{SOURCE2}

%install
cd firmware-qcom-sm7150-ath10k-%{_ath10k_fw_commit}

ath10k-bdencoder -c board-2.json
xz --compress board-2.json

ath10k-fwencoder --create \
	--features=wowlan,no-nwifi-decap-4addr-padding,allows-mesh-bcast,mgmt-tx-by-ref,non-bmi,single-chan-info-per-channel \
	--set-wmi-op-version=tlv --set-htt-op-version=tlv \
	--set-fw-api=5
xz --compress firmware-5.bin

install -Dm644 *.xz -t %{buildroot}/usr/lib/firmware/ath10k/WCN3990/hw1.0
cd ..

cd linux-firmware-%{_linux_fw_commit}
find qca -type f -exec install -Dm644 {}      %{buildroot}/usr/lib/firmware/{} \;
install -Dm644 LICENCE.atheros_firmware       %{buildroot}/usr/share/licenses/atheros-firmware/LICENCE.atheros_firmware
install -Dm644 LICENSE.QualcommAtheros_ath10k %{buildroot}/usr/share/licenses/atheros-firmware/LICENSE.QualcommAtheros_ath10k
install -Dm644 qca/NOTICE.txt                 %{buildroot}/usr/share/licenses/atheros-firmware/NOTICE.txt

%files
/usr/lib/firmware/*
%license /usr/share/licenses/atheros-firmware/LICENCE.atheros_firmware
%license /usr/share/licenses/atheros-firmware/LICENSE.QualcommAtheros_ath10k
%license /usr/share/licenses/atheros-firmware/NOTICE.txt
