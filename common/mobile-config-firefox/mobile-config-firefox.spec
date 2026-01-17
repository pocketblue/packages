Name:           mobile-config-firefox
Version:        4.6.0
Release:        1%{?dist}
Summary:        Mobile and privacy friendly configuration for current standard and extended support releases of Firefox

License:        Mozilla Public License Version 2.0
URL:            https://gitlab.postmarketos.org/postmarketOS/mobile-config-firefox
Source0:         %{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:         mobile-config-autoconfig.patch

BuildRequires:  make

%global debug_package %{nil}

%define extension_dir /var/lib/flatpak/extension/org.mozilla.firefox.systemconfig/%{_arch}/stable

%description
Mobile and privacy friendly configuration for current standard and extended support releases of Firefox

%prep
%autosetup

%build

%install
%make_install FIREFOX_DIR=/usr/lib/firefox
%make_install FIREFOX_DIR=/usr/lib/firefox-esr
%make_install FIREFOX_DIR=/usr/lib/librewolf
%make_install FIREFOX_DIR=%{extension_dir}
cp -r \
    %{?buildroot}/etc/mobile-config-firefox \
    %{?buildroot}/%{extension_dir}/mobile-config-firefox
patch -p1 %{?buildroot}/%{extension_dir}/mobile-config-autoconfig.js < %{SOURCE1}

%files
%license LICENSE
%{_sysconfdir}/{firefox,firefox-esr,librewolf}/policies/policies.json
%{_prefix}/lib/{firefox,firefox-esr,librewolf}/defaults/pref/mobile-config-prefs.js
%{_prefix}/lib/{firefox,firefox-esr,librewolf}/mobile-config-autoconfig.js
%{_sysconfdir}/mobile-config-firefox
%{_datadir}/metainfo/org.postmarketos.mobile_config_firefox.metainfo.xml
%{extension_dir}/*
