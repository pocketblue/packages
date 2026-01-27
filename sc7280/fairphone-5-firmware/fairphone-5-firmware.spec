%global debug_package %{nil}
%global _firmwaredir %{_prefix}/lib/firmware
%global _hexagondir %{_datadir}/qcom/sc7280/Fairphone/FP5
%global commit a4908f548e6f88965e78b1478af1751b6a854fc9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global __requires_exclude ^.*\\.so.*$

Name:           fairphone-5-firmware
Version:        1.0
Release:        1%{?dist}
Summary:        Firmware for Fairphone 5
URL:            https://github.com/FairBlobs/FP5-firmware
Source0:        %{url}/archive/%{commit}/FP5-firmware-%{shortcommit}.tar.gz
Source1:        50-firmware.conf
Source2:        qcom_firmware.files
Source3:        hexagon_firmware.files
BuildArch:      noarch
Requires:       qcom-firmware
AutoReqProv:    no
License:        Unknown

%description
Firmware for Fairphone 5 (codename FP5), including:
- ADSP/CDSP/WPSS firmware for DSP subsystems
- GPU (Adreno 660) zap shader firmware
- Modem firmware
- Audio codec firmware (Awinic AW882xx)
- Bluetooth firmware
- Hexagon filesystem (acdb, dsp modules, sensors)

%prep
%autosetup -n FP5-firmware-%{commit}

%install
mkdir -p %{buildroot}%{_firmwaredir}/qcom/sc7280/Fairphone/FP5 \
         %{buildroot}%{_firmwaredir}/awinic \
         %{buildroot}%{_firmwaredir}/ath11k/WCN6855/hw2.1 \
         %{buildroot}%{_hexagondir}/acdb \
         %{buildroot}%{_hexagondir}/dsp \
         %{buildroot}%{_hexagondir}/sensors \
         %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d

for fw in $(cat %{SOURCE2}); do
    if [ -f "${fw}" ]; then
        install -Dm644 "${fw}" "%{buildroot}%{_firmwaredir}/qcom/sc7280/Fairphone/FP5/$(basename "${fw}")"
    fi
done

for fw in modem.mdt modem.b*; do
    if [ -f "${fw}" ]; then
        install -Dm644 "${fw}" "%{buildroot}%{_firmwaredir}/qcom/sc7280/Fairphone/FP5/$(basename "${fw}")"
    fi
done

if [ -d modem_pr ]; then
    cp -a modem_pr %{buildroot}%{_firmwaredir}/qcom/sc7280/Fairphone/FP5/
fi

if [ -f aw882xx_acf.bin ]; then
    install -Dm644 aw882xx_acf.bin %{buildroot}%{_firmwaredir}/awinic/aw882xx_acf.bin
fi

if [ -f msbtfw11.mbn ]; then
    install -Dm644 msbtfw11.mbn %{buildroot}%{_firmwaredir}/ath11k/WCN6855/hw2.1/msbtfw11.mbn
fi
if [ -f msnv11.bin ]; then
    install -Dm644 msnv11.bin %{buildroot}%{_firmwaredir}/ath11k/WCN6855/hw2.1/msnv11.bin
fi

if [ -d hexagonfs ]; then
    cp -a hexagonfs/acdb/* %{buildroot}%{_hexagondir}/acdb/ 2>/dev/null || true
    cp -a hexagonfs/dsp/* %{buildroot}%{_hexagondir}/dsp/ 2>/dev/null || true
    cp -a hexagonfs/sensors/* %{buildroot}%{_hexagondir}/sensors/ 2>/dev/null || true
    if [ -d hexagonfs/socinfo ]; then
        cp -a hexagonfs/socinfo %{buildroot}%{_hexagondir}/
    fi
fi

find %{buildroot}%{_firmwaredir} -type f -exec chmod 0644 {} \;
find %{buildroot}%{_hexagondir} -type f -exec chmod 0644 {} \;

install -Dm644 %{SOURCE1} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/50-firmware.conf

%files
%{_firmwaredir}/qcom/sc7280/Fairphone
%{_firmwaredir}/awinic
%{_firmwaredir}/ath11k/WCN6855/hw2.1
%{_hexagondir}
%{_prefix}/lib/dracut/dracut.conf.d/50-firmware.conf

%changelog
%autochangelog
