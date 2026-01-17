Name:           regreet-config-hyprland
Version:        2
Release:        0%{?dist}
Summary:        regreet config for hyprland
License:        GPL-3.0-or-later
BuildArch:      noarch
Source1:        config.toml
Source2:        regreet-config-hyprland.conf
Requires:       regreet hyprland

%description
%{summary}

%install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/regreet-config-hyprland/config.toml
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/greetd/regreet-config-hyprland.conf

%post
install -Dpm0644 %{_datadir}/regreet-config-hyprland/config.toml %{_sysconfdir}/greetd/config.toml

%files
%dir %{_datadir}/regreet-config-hyprland
%dir %{_sysconfdir}/greetd
%{_datadir}/regreet-config-hyprland/config.toml
%config(noreplace) %{_sysconfdir}/greetd/regreet-config-hyprland.conf

%changelog
%autochangelog
