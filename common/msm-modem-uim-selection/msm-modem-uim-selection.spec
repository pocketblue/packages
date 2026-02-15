Name:           msm-modem-uim-selection
Version:        1
Release:        1
Summary:        MSM Modem UIM Slot Selection
URL:            https://postmarketos.org/
Source0:        %{name}
Source1:        %{name}.service

License:        GPL-3.0-or-later

Requires:       libqmi
Requires:       libqmi-utils

BuildRequires:  systemd-rpm-macros

%global debug_package %{nil}

%description
%{summary}

%install
install -Dm755 %{SOURCE0} -t %{buildroot}%{_libexecdir}
install -Dm644 %{SOURCE1} -t %{buildroot}%{_unitdir}

%post
%systemd_post                %{name}.service
%preun
%systemd_preun               %{name}.service
%postun
%systemd_postun_with_restart %{name}.service

%files
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
