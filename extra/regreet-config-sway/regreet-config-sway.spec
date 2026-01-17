Name:           regreet-config-sway
Version:        2
Release:        0%{?dist}
Summary:        regreet config for sway
License:        GPL-3.0-or-later
BuildArch:      noarch
Source1:        config.toml
Source2:        regreet-config-sway.conf
Requires:       regreet sway

%description
%{summary}

%install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/regreet-config-sway/config.toml
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/greetd/regreet-config-sway.conf

%post
install -Dpm0644 %{_datadir}/regreet-config-sway/config.toml %{_sysconfdir}/greetd/config.toml

%files
%dir %{_datadir}/regreet-config-sway
%dir %{_sysconfdir}/greetd
%{_datadir}/regreet-config-sway/config.toml
%config(noreplace) %{_sysconfdir}/greetd/regreet-config-sway.conf

%changelog
%autochangelog
