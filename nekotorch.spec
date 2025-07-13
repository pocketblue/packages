%global commit 907046162b6783c3e634ca50d45e68e4f3ca1505
%global id     nekotorch@nekocwd.gitlab.com

Name:          gnome-shell-extension-nekotorch
Version:       48.0
Release:       1%{?dist}
Summary:       flash‑led / torch extension for gnome shell
License:       GPLv3+
URL:           https://gitlab.com/gmanka/NekoTorch
Source0:       %{url}/-/archive/%{commit}/NekoTorch-%{commit}.tar.gz
BuildArch:     noarch
BuildRequires: gnome-shell
BuildRequires: gettext
BuildRequires: unzip
BuildRequires: glib2
BuildRequires: jq
Requires:      udev
Requires:      gsettings-desktop-schemas

%description
flash‑led / torch extension for gnome shell

%prep
%autosetup -n NekoTorch-%{commit}

%install
extpath=%{buildroot}%{_datadir}/gnome-shell/extensions/%{id}
mkdir -p  $extpath
cp -a *.js metadata.json stylesheet.css icons  $extpath/
install -Dm0644 schemas/com.gitlab.nekocwd.nekotorch.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/com.gitlab.nekocwd.nekotorch.gschema.xml
install -Dm0644 99-flash.rules %{buildroot}%{_udevrulesdir}/99-flash.rules

%pre
getent group torch >/dev/null || groupadd -r torch

%post
udevadm control --reload-rules 2>/dev/null || :

%files
%license LICENSE
%doc Readme.md
%{_datadir}/gnome-shell/extensions/%{id}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_udevrulesdir}/99-flash.rules

%changelog
* Fri Jul 11 2025 gmanka 48.0-1
- init
