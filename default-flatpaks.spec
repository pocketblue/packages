Name:           default-flatpaks
Version:        1.0
Release:        1%{?dist}
Summary:        install some flatpaks on first system boot
License:        AGPL-3.0
URL:            https://github.com/gmanka-flatpaks/default-flatpaks
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       flatpak
Requires(post): systemd
Requires(postun): systemd
%{?systemd_user_requires}

%description
install some flatpaks on first system boot

%prep
%autosetup -n %{name}-%{version}
%build
%install
install -Dm0644 apps-list %{buildroot}%{_sysconfdir}/default-flatpaks/apps-list
install -Dm0755 default-flatpaks.sh %{buildroot}%{_bindir}/default-flatpaks
install -Dm0644 default-flatpaks.service %{buildroot}%{_userunitdir}/default-flatpaks.service
install -d -m 1777 %{buildroot}%{_localstatedir}/lib/default-flatpaks

%post
%systemd_user_post default-flatpaks.service

%preun
%systemd_user_preun default-flatpaks.service

%postun
%systemd_user_postun_with_restart default-flatpaks.service

%files
%license license.md
%doc readme.md
%config(noreplace) %{_sysconfdir}/default-flatpaks/apps-list
%{_bindir}/default-flatpaks
%{_userunitdir}/default-flatpaks.service
%dir %attr(1777,root,root) %{_localstatedir}/lib/default-flatpaks
%ghost %{_localstatedir}/lib/default-flatpaks/done

