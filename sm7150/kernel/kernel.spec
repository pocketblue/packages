Name: kernel
ExclusiveArch: aarch64
Version: 6.18.0
Release: 1.sm7150
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
URL: https://github.com/sm7150-mainline/linux

%global _tag %{version}

Source1: %{url}/archive/v%{_tag}.tar.gz
Source2: sm7150.config
License: GPL

Provides: kernel = %{version}-%{release}
Provides: kernel-core = %{version}-%{release}
Provides: kernel-modules = %{version}-%{release}

BuildRequires: kmod, bash, coreutils, tar, git-core, which
BuildRequires: bzip2, xz, findutils, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: zstd
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex, gcc-c++
BuildRequires: rust, rust-src, bindgen, rustfmt, clippy
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: dwarves
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: glibc-static
BuildRequires: rsync
BuildRequires: opencsd-devel >= 1.0.0
BuildRequires: openssl-devel

Requires: dracut >= 027
Requires: bash
Requires: coreutils
Requires: systemd

%description
Mainline kernel for SM7150 platform.

%prep
tar -xzf %{SOURCE1}
cd linux-%{_tag}
cp %{SOURCE2} arch/arm64/configs/sm7150.config

%build
cd linux-%{_tag}
make defconfig sm7150.config -j`nproc`
make EXTRAVERSION="-%{release}" -j`nproc`

%install
cd linux-%{_tag}
uname_r=$(make EXTRAVERSION="-%{release}" kernelrelease)

make EXTRAVERSION="-%{release}" \
     INSTALL_MOD_PATH=%{buildroot}/usr \
     INSTALL_HDR_PATH=%{buildroot}/usr \
     modules_install headers_install

install -d                                            %{buildroot}/usr/lib/modules/$uname_r/dtb/
install -Dm644 arch/arm64/boot/dts/qcom/sm7150-*.dtb  %{buildroot}/usr/lib/modules/$uname_r/dtb/
install -Dm644 arch/arm64/boot/vmlinuz                %{buildroot}/usr/lib/modules/$uname_r/vmlinuz
install -Dm644 System.map                             %{buildroot}/usr/lib/modules/$uname_r/System.map
install -Dm644 .config                                %{buildroot}/usr/lib/modules/$uname_r/config

install -d %{buildroot}/usr/lib/kernel
install -d %{buildroot}/usr/lib/ostree-boot

rm %{buildroot}/usr/lib/modules/%{version}*/build

%files
/usr/lib/modules/%{version}*

%posttrans
dracut -f --kver %{version}-%{release} /usr/lib/modules/%{version}-%{release}/initramfs.img
kernel-install add %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz /usr/lib/modules/%{version}-%{release}/initramfs.img

%postun
kernel-install remove %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz

%package core
License: GPL
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
Requires: kernel

%description core
Mainline kernel for SM7150 platform.

%files core


%package modules
License: GPL
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
Requires: kernel

%description modules
Mainline kernel for SM7150 platform.

%files modules


%package devel
License: GPL
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
Requires: kernel-headers

%description devel
Mainline kernel header for SM7150 platform.

%files devel


%package headers
License: GPL
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
Provides: kernel-devel = %{version}-%{release}

%description headers
Mainline kernel headers for SM7150 platform.

%files headers
/usr/include


%package devel-matched
License: GPL
Summary: AIO package for linux kernel, modules and headers for SM7150 platform.
Requires: kernel-devel
Requires: kernel-core

%description devel-matched
Mainline kernel headers for SM7150 platform.

%files devel-matched

