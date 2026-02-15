Name:           q6voiced
Version:        0.2.0
Release:        2
Summary:        A userspace daemon for the QDSP6 voice call audio driver

License:        MIT
URL:            https://gitlab.postmarketos.org/postmarketOS/q6voiced
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

Source1:        %{name}.service
Source2:        %{name}@.service

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-devel
BuildRequires:  systemd-rpm-macros

Requires:       alsa-lib
Requires:       dbus

%description
A userspace daemon for the QDSP6 voice call audio driver

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 %{SOURCE1} -t %{buildroot}%{_unitdir}/
install -Dm644 %{SOURCE2} -t %{buildroot}%{_unitdir}/

%post
%systemd_post %{name}.service %{name}@.service

%preun
%systemd_preun %{name}.service %{name}@.service

%postun
%systemd_postun_with_restart %{name}.service %{name}@.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service

%changelog
%autochangelog
