Name: sdm845-firmware-symlinks
Version:   1
Release:   1%{?dist}
Summary:   symlinks for sdm845 firmware
License:   GPLv2
BuildArch: noarch

%description
%{summary}

%install
mkdir -p %{buildroot}/usr/lib/firmware/{qcom/sdm845/{OnePlus,Xiaomi},qca/OnePlus}
ln -s /usr/lib/firmware/updates/qcom/sdm845/oneplus6 %{buildroot}/usr/lib/firmware/qcom/sdm845/OnePlus/enchilada
ln -s /usr/lib/firmware/updates/qcom/sdm845/beryllium %{buildroot}/usr/lib/firmware/qcom/sdm845/Xiaomi/beryllium
ln -s /usr/lib/firmware/updates/qca/oneplus6 %{buildroot}/usr/lib/firmware/qca/OnePlus/enchilada

%files
/usr/lib/firmware/qcom/sdm845/OnePlus/enchilada
/usr/lib/firmware/qcom/sdm845/Xiaomi/beryllium
/usr/lib/firmware/qca/OnePlus/enchilada

%changelog
%autochangelog
