Name:             usb-gadget
Version:          1
Release:          1%{?dist}
Summary:          USB gadget network and serial service
License:          AGPL-3.0-or-later
URL:              https://github.com/pocketblue/packages
Source0:          usb-gadget-start
Source1:          usb-gadget-stop
Source2:          usb-gadget.service
Source3:          dnsmasq-usb-network.conf
BuildArch:        noarch
Requires:         bash dnsmasq iproute
Requires(post):   systemd
Requires(postun): systemd
BuildRequires:    systemd-rpm-macros

%description
USB gadget service that configures USB networking and serial access

%install
install -Dm755 %{SOURCE0} -t %{buildroot}%{_bindir}
install -Dm755 %{SOURCE1} -t %{buildroot}%{_bindir}
install -Dm644 %{SOURCE2} -t %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE3} -t %{buildroot}%{_sysconfdir}

%post
%systemd_post usb-gadget.service

%preun
%systemd_preun usb-gadget.service

%postun
%systemd_postun_with_restart usb-gadget.service

%files
%{_bindir}/usb-gadget-start
%{_bindir}/usb-gadget-stop
%{_unitdir}/usb-gadget.service
%config(noreplace) %{_sysconfdir}/dnsmasq-usb-network.conf

%changelog
%autochangelog
