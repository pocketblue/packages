%global _commit 8205db9b0e34f9be5064c9244cc5ad94c4aca9a6

Name: kernel
ExclusiveArch: aarch64
Version: 7.1.7
Release: 1.pipa%{?dist}
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
URL: https://github.com/PipaDB/linux
Source1: %{url}/archive/%{_commit}/linux-%{_commit}.tar.gz
Source2: pipa.config
License: GPL-2.0-only

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

Requires: dracut
Requires: bash
Requires: coreutils
Requires: systemd
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-modules = %{version}-%{release}



%description
Mainline kernel for Xiaomi Pad 6 (pipa).

%prep
tar -xzf %{SOURCE1}
cd linux-%{_commit}
cp %{SOURCE2} .config

%build
cd linux-%{_commit}
cp %{SOURCE2} .config
make olddefconfig

make EXTRAVERSION="-%{release}" -j%{_smp_build_ncpus} Image.gz modules dtbs

%install
cd linux-%{_commit}
kernel_version=$(make EXTRAVERSION="-%{release}" kernelrelease)

mkdir -p %{buildroot}/boot/
cp arch/arm64/boot/Image.gz %{buildroot}/boot/vmlinuz-$kernel_version
cp System.map %{buildroot}/boot/System.map-$kernel_version
cp .config %{buildroot}/boot/config-$kernel_version

make EXTRAVERSION="-%{release}" modules_install INSTALL_MOD_PATH=%{buildroot}/usr DEPMOD=true
cp arch/arm64/boot/dts/qcom/sm8250-xiaomi-pipa.dtb %{buildroot}/usr/lib/modules/$kernel_version/devicetree
ln -s ./devicetree %{buildroot}/usr/lib/modules/$kernel_version/dtb
cp arch/arm64/boot/Image.gz %{buildroot}/usr/lib/modules/$kernel_version/vmlinuz
make EXTRAVERSION="-%{release}" headers_install INSTALL_HDR_PATH=%{buildroot}/usr
rm -f %{buildroot}/usr/lib/modules/$kernel_version/build
rm -f %{buildroot}/usr/lib/modules/$kernel_version/source

%files


%package core
License: GPL-2.0-only
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).


%description core
Mainline kernel for Xiaomi Pad 6 (pipa).

%files core
/boot/System.map-%{version}-%{release}
/boot/config-%{version}-%{release}
/boot/vmlinuz-%{version}-%{release}

%posttrans core
/sbin/depmod -a %{version}-%{release}
dracut -f --kver %{version}-%{release} /usr/lib/modules/%{version}-%{release}/initramfs.img
kernel-install add %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz /usr/lib/modules/%{version}-%{release}/initramfs.img


%postun core
kernel-install remove %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz


%package modules
License: GPL-2.0-only
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Requires: %{name}-core = %{version}-%{release}

%description modules
Mainline kernel for Xiaomi Pad 6 (pipa).

%files modules
/usr/lib/modules/%{version}-%{release}/

%package headers
License: GPL-2.0-only
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).

%description headers
Mainline kernel headers for Xiaomi Pad 6 (pipa).

%files headers
/usr/include/
