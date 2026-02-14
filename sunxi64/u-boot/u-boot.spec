%undefine _debugsource_packages
%global _default_patch_fuzz 2

%global tfa_version 2.14.0
%global crust_version 0.6
%global plat sun50i_h6

%global armbian_build_commit e77884838966ed59aaf6cf73c29df7a0b08a8d32
%global armbian_build_raw https://github.com/armbian/build/raw/%{armbian_build_commit}

%global cross_compile %{nil}
%global target_cc gcc
%global crust_cross_compile openrisc-linux-gnu-
%if "%{_build_cpu}" != "%{_target_cpu}"
%global cross_compile aarch64-linux-gnu-
%global target_cc %{cross_compile}gcc
%endif

Version:        2026.01
Release:        5.%{plat}%{?dist}
ExclusiveArch:  aarch64
Name:           u-boot
Summary:        U-Boot bootloader for the Orange Pi 3 LTS (Allwinner H6).
License:        GPL-2.0-or-later
URL:            https://www.denx.de/wiki/U-Boot

Source0:        https://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
Source1:        https://github.com/ARM-software/arm-trusted-firmware/archive/refs/tags/v%{tfa_version}.tar.gz
Source2:        https://github.com/crust-firmware/crust/archive/refs/tags/v%{crust_version}.tar.gz
Source3:        u-boot-install-orangepi3-lts.sh

Patch1:         %{armbian_build_raw}/patch/u-boot/v%{version}/board_orangepi3-lts/001-Add-board-OrangePi-3-LTS.patch
Patch2:         %{armbian_build_raw}/patch/u-boot/v%{version}/board_orangepi3-lts/002-Add-OrangePi-3-LTS-defconfig.patch
Patch3:         %{armbian_build_raw}/patch/u-boot/v%{version}/board_orangepi3-lts/003-mmc-increase-stabilization-delay-from-1ms-to-20ms.patch

Requires:       bash coreutils util-linux
BuildRequires:  bc bison flex gcc make openssl-devel python3 python3-devel python3-pyyaml python3-setuptools swig binutils-aarch64-linux-gnu gcc-aarch64-linux-gnu binutils-openrisc-linux-gnu gcc-openrisc-linux-gnu

%description
%{summary}

%prep
%setup -q -n u-boot-%{version} -a1 -a2
%autopatch -p1

%build
pushd arm-trusted-firmware-%{tfa_version}
make -j%{?_smp_build_ncpus} PLAT=%{plat} CC=%{target_cc} CROSS_COMPILE=%{cross_compile} CFLAGS= LDFLAGS=
popd

pushd crust-%{crust_version}
make pine_h64_defconfig CROSS_COMPILE=%{crust_cross_compile}
make -j%{?_smp_build_ncpus} scp CROSS_COMPILE=%{crust_cross_compile}
popd

make orangepi_3_lts_defconfig CC=%{target_cc} CROSS_COMPILE=%{cross_compile} HOSTCC=gcc HOSTCFLAGS= HOSTLDFLAGS= CFLAGS= LDFLAGS=
./scripts/config --disable TOOLS_KWBIMAGE --disable TOOLS_LIBCRYPTO --disable TOOLS_MKEFICAPSULE
make -j%{?_smp_build_ncpus} BL31=arm-trusted-firmware-%{tfa_version}/build/%{plat}/release/bl31.bin SCP=crust-%{crust_version}/build/scp/scp.bin CC=%{target_cc} CROSS_COMPILE=%{cross_compile} HOSTCC=gcc HOSTCFLAGS= HOSTLDFLAGS= CFLAGS= LDFLAGS=

%install
install -Dm 0644 u-boot-sunxi-with-spl.bin %{buildroot}/usr/lib/u-boot/orangepi3-lts/u-boot-sunxi-with-spl.bin
install -Dm 0755 %{SOURCE3} %{buildroot}/usr/lib/u-boot/orangepi3-lts-install-uboot

%post
if [ "${UBOOT_INSTALL_SKIP:-0}" != "1" ]; then
    /usr/lib/u-boot/orangepi3-lts-install-uboot
fi

%files
%license Licenses/README
%doc README
/usr/lib/u-boot/orangepi3-lts/u-boot-sunxi-with-spl.bin
/usr/lib/u-boot/orangepi3-lts-install-uboot

%changelog
%autochangelog
