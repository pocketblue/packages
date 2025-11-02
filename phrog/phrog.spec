%global cargo_install_lib 0
%global commit 51ca5a389d7224fd7527490f57253c0c42735d35

Name:           phrog
Version:        0.46.0
Release:        3
Summary:        Mobile-friendly greeter for greetd
License:        GPL-3.0-only
URL:            https://github.com/samcday/phrog
Source0:        %{url}/archive/%{commit}.tar.gz
Source1:        %{name}-0.46.0-vendor.tar.xz

BuildRequires:  cargo-rpm-macros
BuildRequires:  libphosh-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)

Requires:       accountsservice
Requires:       gnome-session
Requires:       greetd
Requires:       phoc

%description
Phrog uses Phosh and greetd to provide a graphical login manager.

%prep
%autosetup -n %{name}-%{commit} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%{__install} -Dpm 0644 data/mobi.phosh.phrog.gschema.xml -t %{buildroot}%{_datadir}/glib-2.0/schemas/
%{__install} -Dpm 0644 data/phrog.session -t %{buildroot}%{_datadir}/gnome-session/sessions/
%{__install} -Dpm 0644 data/mobi.phosh.Phrog.desktop -t %{buildroot}%{_datadir}/applications/
%{__install} -Dpm 0644 data/mobi.phosh.Phrog.service -t %{buildroot}%{_userunitdir}
%{__install} -Dpm 0644 data/mobi.phosh.Phrog.target -t %{buildroot}%{_userunitdir}
%{__install} -Dpm 0644 dist/fedora/greetd-config.toml -t %{buildroot}%{_sysconfdir}/phrog/
%{__install} -Dpm 0644 dist/fedora/phrog.service -t %{buildroot}%{_unitdir}/
%{__install} -Dpm 0644 data/systemd-session.conf -T %{buildroot}%{_userunitdir}/gnome-session@phrog.target.d/session.conf
%{__install} -Dpm 0755 data/phrog-greetd-session -t %{buildroot}%{_libexecdir}/
%{__install} -d %{buildroot}%{_datadir}/phrog/autostart
%{__install} -d %{buildroot}%{_sysconfdir}/phrog/autostart
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/phrog
%{_datadir}/applications/mobi.phosh.Phrog.desktop
%{_datadir}/glib-2.0/schemas/mobi.phosh.phrog.gschema.xml
%{_datadir}/gnome-session/sessions/phrog.session
%{_datadir}/phrog
%{_datadir}/phrog/autostart
%{_libexecdir}/phrog-greetd-session
%{_sysconfdir}/phrog
%{_sysconfdir}/phrog/autostart
%config(noreplace) %{_sysconfdir}/phrog/greetd-config.toml
%{_unitdir}/phrog.service
%{_userunitdir}/gnome-session@phrog.target.d/session.conf
%{_userunitdir}/mobi.phosh.Phrog.service
%{_userunitdir}/mobi.phosh.Phrog.target

%changelog
%autochangelog
