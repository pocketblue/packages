%undefine        _debugsource_packages
%global _default_patch_fuzz 2
%global soc      sunxi64
%global armbian_build_commit 6f022174747f14f1b022f0eb707ff35cf1f5133c
%global armbian_build_raw https://github.com/armbian/build/raw/%{armbian_build_commit}
Version:         6.18.6
Release:         9.%{soc}%{?dist}
ExclusiveArch:   aarch64
Name:            kernel
Summary:         mainline kernel for %{soc}
License:         GPLv2
URL:             https://cdn.kernel.org/pub/linux/kernel
Source0:         %{url}/v6.x/linux-%{version}.tar.xz
Source1:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/dt_64/sun50i-h6-orangepi-3-lts.dts
Source2:         %{armbian_build_raw}/config/kernel/linux-%{soc}-current.config
Source3:         armbian.config
Source4:         extra-%{soc}.config

Patch1:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-allwinner-v6.3.patch
Patch2:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-allwinner-bugfix-v6.3.patch
Patch3:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-allwinner-v6.3-compilation-fix.patch
Patch4:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.4-post.patch
Patch5:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-warnings.patch
Patch6:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-park-link-v6.1-post.patch
Patch7:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.1.patch
Patch8:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.6-fix-tty-sdio.patch
Patch9:          %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-fix-setting-mac-address-for-netdev.patch
Patch10:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/wireless-uwe5622-Fix-compilation-with-6.7-kernel.patch
Patch11:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/wireless-uwe5622-reduce-system-load.patch
Patch12:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.9.patch
Patch13:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.11.patch
Patch14:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-fix-spanning-writes.patch
Patch15:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-fix-timer-api-changes-for-6.15-only-sunxi.patch
Patch16:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.16.patch
Patch17:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.17.patch
Patch18:         %{armbian_build_raw}/patch/misc/wireless-uwe5622/uwe5622-v6.18.patch
Patch19:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/hdmi-audio-6.18/0010-arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch
Patch20:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/modem-6.18/0001-misc-modem-power-Power-manager-for-modems.patch
Patch21:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/opi3-eth-6.18/0001-net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regu.patch
Patch22:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/opi3-eth-6.18/0002-net-stmmac-sun8i-Rename-PHY-regulator-variable-to-re.patch
Patch23:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/opi3-eth-6.18/0003-net-stmmac-sun8i-Add-support-for-enabling-a-regulato.patch
Patch24:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.megous/opi3-eth-6.18/0004-arm64-dts-allwinner-orange-pi-3-Enable-ethernet.patch
Patch25:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.armbian/0401-arm64-dts-sun50i-h6-add-ac200-ephy.patch
Patch26:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.armbian/0402-arm64-dts-sun50i-h6-add-ac200-codec.patch
Patch27:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.armbian/arm64-dts-sun50i-h6-h616-add-sunxi-info-nodes.patch
Patch28:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.armbian/drv-misc-sunxi-add-addr-mgt-driver-uwe5622.patch
Patch29:         %{armbian_build_raw}/patch/kernel/archive/sunxi-6.18/patches.armbian/drv-nvmem-sunxi-add-chipid-serial-helpers.patch

Provides:        kernel               = %{version}-%{release}
Provides:        kernel-core          = %{version}-%{release}
Provides:        kernel-devel         = %{version}-%{release}
Provides:        kernel-headers       = %{version}-%{release}
Provides:        kernel-modules       = %{version}-%{release}
Provides:        kernel-modules-core  = %{version}-%{release}

BuildRequires:   bc bison dwarves diffutils elfutils-devel findutils gcc gcc-c++ git-core hmaccalc hostname make openssl-devel perl-interpreter rsync tar which flex bzip2 xz zstd python3 python3-devel python3-pyyaml rust rust-src bindgen rustfmt clippy opencsd-devel net-tools

%global uname_r %{version}-%{release}.%{_target_cpu}

%description
%{summary}

%prep
%autosetup -n linux-%{version} -N
install -Dm644 %{SOURCE1} arch/arm64/boot/dts/allwinner/sun50i-h6-orangepi-3-lts.dts
echo 'dtb-$(CONFIG_ARCH_SUNXI) += sun50i-h6-orangepi-3-lts.dtb' >> arch/arm64/boot/dts/allwinner/Makefile
%autopatch -p1
echo 'obj-$(CONFIG_SPARD_WLAN_SUPPORT) += uwe5622/' >> drivers/net/wireless/Makefile
./scripts/kconfig/merge_config.sh -O . %{SOURCE2} %{SOURCE3} %{SOURCE4}
sed -i '/^CONFIG_LOCALVERSION=/d' .config

%build
make olddefconfig
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= -j%{?_smp_build_ncpus} Image modules dtbs

%install
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= INSTALL_MOD_PATH=%{buildroot}/usr INSTALL_HDR_PATH=%{buildroot}/usr modules_install headers_install
install -Dm644 arch/arm64/boot/dts/allwinner/sun50i-h6-orangepi-3-lts.dtb %{buildroot}/usr/lib/modules/%{uname_r}/devicetree
install -Dm644 arch/arm64/boot/Image %{buildroot}/usr/lib/modules/%{uname_r}/vmlinuz
install -Dm644 System.map            %{buildroot}/usr/lib/modules/%{uname_r}/System.map
install -Dm644 .config               %{buildroot}/usr/lib/modules/%{uname_r}/config
install -d %{buildroot}/usr/lib/kernel
install -d %{buildroot}/usr/lib/ostree-boot

%files
/usr/include
/usr/lib/modules/%{uname_r}

%posttrans
set -e
depmod -a %{uname_r}
dracut /usr/lib/modules/%{uname_r}/initramfs.img %{uname_r}
kernel-install add %{uname_r} /usr/lib/modules/%{uname_r}/vmlinuz /usr/lib/modules/%{uname_r}/initramfs.img

%changelog
%autochangelog
