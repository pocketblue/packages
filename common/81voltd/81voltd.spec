Name:           81voltd
Version:        1.2.0
Release:        1
Summary:        Simple implementation of the IMS Data service on QMI/QRTR

License:        GPL-2.0-or-later
URL:            https://gitlab.postmarketos.org/modem/%{name}
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ModemManager-devel
BuildRequires:  ModemManager-glib-devel
BuildRequires:  libqmi-devel
BuildRequires:  libqmi-utils
BuildRequires:  qrtr-devel
BuildRequires:  systemd-rpm-macros

%description
%{summary}

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
rm %{buildroot}/etc/init.d/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
