%global commit 206214916c796df6842a5df1d95ae580881ce603
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           hciattach-opi
Version:        1.0
Release:        2.git%{shortcommit}%{?dist}
ExclusiveArch:  aarch64
Summary:        hciattach_opi helper for UWE5622 Bluetooth
License:        GPL-2.0-only
URL:            https://github.com/orangepi-xunlong/orangepi-build
Source0:        %{url}/archive/%{commit}/orangepi-build-%{commit}.tar.gz
BuildRequires:  gcc make bluez-libs-devel

%description
%{summary}

%prep
%autosetup -n orangepi-build-%{commit}

%build
make -C external/cache/sources/hcitools hciattach_opi CFLAGS="%{optflags} -I. -Ilib -Ilib/bluetooth -DVERSION=\\\"5.10\\\" -Wno-strict-aliasing -Wno-int-conversion -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D_REENTRANT -include sys/uio.h -include sys/time.h"

%install
install -Dm 0755 external/cache/sources/hcitools/output/hciattach_opi %{buildroot}/%{_bindir}/hciattach_opi

%files
%license external/cache/sources/hcitools/NOTICE
%{_bindir}/hciattach_opi

%changelog
%autochangelog
