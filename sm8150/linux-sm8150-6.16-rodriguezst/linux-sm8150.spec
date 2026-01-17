%undefine        _debugsource_packages
%global soc      sm8150
Version:         6.16.0
Release:         6.rodriguezst.%{soc}%{?dist}
ExclusiveArch:   aarch64
Name:            kernel
Summary:         mainline kernel for %{soc}
License:         GPLv2
URL:             https://github.com/rodriguezst/linux
Source0:         %{url}/archive/refs/heads/v%{version}-nabu.tar.gz
Source1:         extra-%{soc}.config
Patch0:          rotation.patch

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
%autosetup -n linux-%{version}-nabu -p1
make defconfig %{soc}.config

%build
sed -i '/^CONFIG_LOCALVERSION=/d' .config
cat %{SOURCE1} >> .config
make olddefconfig
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= -j%{?_smp_build_ncpus} Image modules dtbs

%install
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= INSTALL_MOD_PATH=%{buildroot}/usr INSTALL_HDR_PATH=%{buildroot}/usr modules_install headers_install
install -Dm644 arch/arm64/boot/dts/qcom/%{soc}-xiaomi-nabu.dtb %{buildroot}/usr/lib/modules/%{uname_r}/devicetree
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
