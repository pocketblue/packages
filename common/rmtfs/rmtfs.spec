Name:           rmtfs
Version:        1.1.1
Release:        %autorelease
Summary:        Qualcomm Remote Filesystem Service Implementation

License:        BSD-3-Clause
URL:            https://github.com/linux-msm/rmtfs/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  qrtr-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

Requires: qrtr

%description
Qualcomm Remote Filesystem Service Implementation.

%prep
%autosetup -p1

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

%post
%systemd_post rmtfs.service rmtfs-dir.service

%preun
%systemd_preun rmtfs.service rmtfs-dir.service

%postun
%systemd_postun rmtfs.service rmtfs-dir.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/rmtfs.service
%{_unitdir}/rmtfs-dir.service

%changelog
%autochangelog
