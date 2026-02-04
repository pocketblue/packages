Name:           make-dynpart-mappings
Version:        10.2.4
Release:        %autorelease
Summary:        A command-line tool that uses the device mapper to make block devices based on dynamic partitions
URL:            https://gitlab.com/flamingradian/%{name}
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}@.service

# exceptions:
# 3rdparty/*: Apache-2.0
License:        GPL-3.0-only

Requires:       device-mapper-libs
Requires:       libblkid
Requires:       libmd

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libmd-devel
BuildRequires:  lvm2-devel
BuildRequires:  libblkid-devel
BuildRequires:  systemd-rpm-macros

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup

%build
%make_build

%install
install -Dm755 %{name} -t %{buildroot}%{_bindir}
install -Dm644 %{SOURCE1} -t %{buildroot}%{_unitdir}

%post
%systemd_post                %{name}@.service
%preun
%systemd_preun               %{name}@.service
%postun
%systemd_postun_with_restart %{name}@.service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service

%changelog
%autochangelog
