Name:             default-flatpaks
Version:          2.0
Release:          0%{?dist}
Summary:          Install default Flatpak applications on first boot
License:          AGPL-3.0
URL:              https://github.com/pocketblue/packages
Source0:          flatpak-preinstall.service
Source1:          pocketblue.preinstall
Source2:          90-default-flatpaks.preset
Source3:          default-flatpaks.conf
BuildArch:        noarch
Requires:         flatpak dbus-daemon
Requires(post):   systemd
Requires(postun): systemd
BuildRequires:    systemd-rpm-macros
%{?systemd_requires}

%description
%{summary}

%install
install -Dm0644 %{SOURCE0} -t %{buildroot}%{_unitdir}
install -Dm0644 %{SOURCE1} -t %{buildroot}%{_datadir}/flatpak/preinstall.d
install -Dm0644 %{SOURCE2} -t %{buildroot}%{_prefix}/lib/systemd/system-preset
install -Dm0644 %{SOURCE3} -t %{buildroot}%{_tmpfilesdir}

%post
%systemd_post      flatpak-preinstall.service
%tmpfiles_create   %{_tmpfilesdir}/default-flatpaks.conf

%preun
%systemd_preun      flatpak-preinstall.service

%postun
%systemd_postun_with_restart      flatpak-preinstall.service

%files
%{_unitdir}/flatpak-preinstall.service
%{_datadir}/flatpak/preinstall.d/pocketblue.preinstall
%{_prefix}/lib/systemd/system-preset/90-default-flatpaks.preset
%{_tmpfilesdir}/default-flatpaks.conf
%ghost %{_localstatedir}/lib/default-flatpaks/default-flatpaks-initialized

%changelog
%autochangelog
