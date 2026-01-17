%global debug_package %{nil}
%global commit        428184b45f1294a0e66979f570902de84883e1fc
Name:                 nothing-spacewar-firmware
Version:              1
Release:              0%{?dist}
Summary:              firmware for nothing phone 1
URL:                  https://github.com/mainlining/firmware-nothing-spacewar
Source0:              %{url}/archive/%{commit}.tar.gz
BuildArch:            noarch
Requires:             qcom-firmware
AutoReqProv:          no
License:              Unknown
# https://github.com/NothingOSS/android_kernel_msm-5.4_nothing_sm7325/issues/15

%description
%{summary}

%prep
%autosetup -n firmware-nothing-spacewar-%{commit}

%install
find . -type f -exec install -Dm644 {} %{buildroot}/{} ';'

%files
/lib/firmware/qcom
/usr/share/qcom

%changelog
%autochangelog
