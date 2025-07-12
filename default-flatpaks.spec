Name:             default-flatpaks
Version:          1.7
Release:          1%{?dist}
Summary:          install some flatpaks on first system boot
License:          AGPL-3.0
URL:              https://github.com/gmanka-flatpaks/default-flatpaks
Source0:          %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:        noarch
Requires:         flatpak libnotify
Requires(post):   systemd
Requires(postun): systemd
BuildRequires:    systemd-rpm-macros
%{?systemd_requires}
%{?systemd_user_requires}

%description
install some flatpaks on first system boot

%prep
%autosetup -n %{name}-%{version}
%build
%install
install -Dm0644 apps-list %{buildroot}%{_sysconfdir}/default-flatpaks/apps-list
install -Dm0755 default-flatpaks.sh %{buildroot}%{_bindir}/default-flatpaks
install -Dm0644 default-flatpaks.tmpfiles %{buildroot}%{_tmpfilesdir}/default-flatpaks.conf
install -Dm0644 flatpak-add-flathub-repo.service %{buildroot}%{_unitdir}/flatpak-add-flathub-repo.service
install -Dm0644 default-flatpaks.service %{buildroot}%{_userunitdir}/default-flatpaks.service
install -Dm0644 90-default-flatpaks.preset %{buildroot}%{_prefix}/lib/systemd/user-preset/90-default-flatpaks.preset
install -Dm0644 90-flatpak-add-flathub-repo.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/90-flatpak-add-flathub-repo.preset

%post
%systemd_post      flatpak-add-flathub-repo.service
%systemd_user_post default-flatpaks.service
%tmpfiles_create   %{_tmpfilesdir}/default-flatpaks.conf

%preun
%systemd_preun      flatpak-add-flathub-repo.service
%systemd_user_preun default-flatpaks.service

%postun
%systemd_postun_with_restart      flatpak-add-flathub-repo.service
%systemd_user_postun_with_restart default-flatpaks.service

%files
%license license.md
%doc readme.md
%config(noreplace) %{_sysconfdir}/default-flatpaks/apps-list
%{_tmpfilesdir}/default-flatpaks.conf
%{_bindir}/default-flatpaks
%{_unitdir}/flatpak-add-flathub-repo.service
%{_userunitdir}/default-flatpaks.service
%{_prefix}/lib/systemd/system-preset/90-flatpak-add-flathub-repo.preset
%{_prefix}/lib/systemd/user-preset/90-default-flatpaks.preset
%ghost %{_localstatedir}/lib/default-flatpaks/initialized
