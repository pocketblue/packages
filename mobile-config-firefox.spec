Name:           mobile-config-firefox
Version:        4.6.0
Release:        1%{?dist}
Summary:        Mobile and privacy friendly configuration for current standard and extended support releases of Firefox

License:        Mozilla Public License Version 2.0
URL:            https://gitlab.postmarketos.org/postmarketOS/mobile-config-firefox
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make

%description
Mobile and privacy friendly configuration for current standard and extended support releases of Firefox

%prep
%autosetup

%build

%install
%make_install FIREFOX_DIR=/usr/lib/firefox
%make_install FIREFOX_DIR=/usr/lib/firefox-esr
%make_install FIREFOX_DIR=/usr/lib/librewolf

%files
%license LICENSE
%{_sysconfdir}/{firefox,firefox-esr,librewolf}/policies/policies.json
%{_prefix}/lib/{firefox,firefox-esr,librewolf}/defaults/pref/mobile-config-prefs.js
%{_prefix}/lib/{firefox,firefox-esr,librewolf}/mobile-config-autoconfig.js
%{_sysconfdir}/mobile-config-firefox
%{_datadir}/metainfo/org.postmarketos.mobile_config_firefox.metainfo.xml
