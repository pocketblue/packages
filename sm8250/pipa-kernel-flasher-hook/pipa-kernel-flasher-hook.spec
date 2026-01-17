Name: pipa-kernel-flasher-hook
Version: 1.2
Release: 1
Summary: Kernel flasher hook for the Xiaomi Pad 6
Source1: 99-android-boot.install
License: MIT

Requires: android-tools
Requires: qbootctl

%description
Kernel flasher hook for the Xiaomi Pad 6

%install
install -Dm755 %{SOURCE1} %{buildroot}/usr/lib/kernel/install.d/99-android-boot.install

%files
/usr/lib/kernel/install.d/99-android-boot.install
