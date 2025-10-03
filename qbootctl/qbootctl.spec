Name:           qbootctl
Version:        0.2.2
Release:        2%{?dist}
Summary:        CLI tool for manipulating A/B slots on Android devices
License:        GPL-3.0-or-later
URL:            https://github.com/linux-msm/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        90-%{name}.preset

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

%description
%{summary}. It is a port of the original Android bootctrl HAL developed by
Qualcomm, modified to build on Linux and provide a friendly CLI interface.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 %{SOURCE1} -t %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE2} -t %{buildroot}%{_prefix}/lib/systemd/system-preset

%post
%systemd_post                %{name}.service
%preun
%systemd_preun               %{name}.service
%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_prefix}/lib/systemd/system-preset/90-%{name}.preset

%changelog
%autochangelog
