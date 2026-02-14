%undefine      _debugsource_packages
%global soc    sc7280
%global commit 2f12f5e50225dcd556455e7a4dc4751832b7be88
Version:       6.19.0
Release:       903.%{soc}%{?dist}
ExclusiveArch: aarch64
Name:          kernel
Summary:       mainline kernel for %{soc}
License:       GPLv2
URL:           https://github.com/sc7280-mainline/linux
Source0:       %{url}/archive/%{commit}.tar.gz
Source1:       config-fp5.aarch64

Provides:      kernel               = %{version}-%{release}
Provides:      kernel-core          = %{version}-%{release}
Provides:      kernel-devel         = %{version}-%{release}
Provides:      kernel-headers       = %{version}-%{release}
Provides:      kernel-modules       = %{version}-%{release}
Provides:      kernel-modules-core  = %{version}-%{release}

BuildRequires: bc bison dwarves diffutils elfutils-devel findutils gcc gcc-c++ git-core hmaccalc hostname make openssl openssl-devel perl-interpreter rsync tar which flex bzip2 xz zstd python3 python3-devel python3-pyyaml rust rust-src bindgen rustfmt clippy opencsd-devel net-tools glibc-static

%global uname_r %{version}-%{release}.%{_target_cpu}

%description
mainline kernel for %{soc}

%prep
%autosetup -n linux-%{commit}

%build
cp %{SOURCE1} .config
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= -j%{?_smp_build_ncpus} Image modules dtbs

%install
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= INSTALL_MOD_PATH=%{buildroot}/usr INSTALL_HDR_PATH=%{buildroot}/usr INSTALL_DTBS_PATH=%{buildroot}/usr/lib/modules/%{uname_r}/dtbs modules_install headers_install dtbs_install
install -Dm644 arch/arm64/boot/Image %{buildroot}/usr/lib/modules/%{uname_r}/vmlinuz
install -Dm644 System.map            %{buildroot}/usr/lib/modules/%{uname_r}/System.map
install -Dm644 .config               %{buildroot}/usr/lib/modules/%{uname_r}/config
install -d %{buildroot}/usr/lib/kernel
install -d %{buildroot}/usr/lib/ostree-boot

%files
/usr/include
/usr/lib/modules/%{uname_r}

%posttrans
depmod -a -v %{uname_r}

%changelog
%autochangelog
