%global dracutlibdir %{_prefix}/lib/dracut
Name:             usb-shell
Version:          1
Release:          1%{?dist}
summary:          emergency shell enables usb serial and drops you to bash
License:          AGPL-3.0-only
URL:              https://github.com/pocketblue/packages/tree/main/common/usb-shell
Source0:          module-setup.sh
Source1:          %{name}
Source2:          %{name}.service
Source3:          90-%{name}-dracut.conf
Source4:          90-%{name}-service.conf
BuildArch:        noarch
Requires:         bash coreutils dracut ostree systemd util-linux-core

%description
dracut module that starts an interactive root shell on /dev/ttyGS0
when initramfs enters emergency mode

%prep
%setup -q -c -T

%install
install -Dm755 %{SOURCE0} %{SOURCE1} \
  -t %{buildroot}%{dracutlibdir}/modules.d/99%{name}
install -Dm644 %{SOURCE2} %{SOURCE4} \
  -t %{buildroot}%{dracutlibdir}/modules.d/99%{name}
install -Dm644 %{SOURCE3} \
  -t %{buildroot}%{dracutlibdir}/dracut.conf.d

%files
%{dracutlibdir}/modules.d/99%{name}/
%{dracutlibdir}/dracut.conf.d/90-%{name}-dracut.conf

%changelog
%autochangelog
