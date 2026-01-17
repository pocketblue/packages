Name:             ath10k-shutdown
Version:          1
Release:          1%{?dist}
Summary:          disable ath10k modules on shutdown
License:          AGPL-3.0
URL:              https://github.com/pocketblue/packages
Source0:          %{name}.service
Source1:          90-%{name}.preset
BuildArch:        noarch
Requires(post):   systemd
Requires(postun): systemd
BuildRequires:    systemd-rpm-macros

%description
ensure that ath10k modules are disabled before shutdown, required for proper shutdown process on oneplus6 and mipad5

%install
install -Dm644 %{SOURCE0} -t %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE1} -t %{buildroot}%{_prefix}/lib/systemd/system-preset

%post
%systemd_post                %{name}.service
%preun
%systemd_preun               %{name}.service
%postun
%systemd_postun_with_restart %{name}.service

%files
%{_unitdir}/%{name}.service
%{_prefix}/lib/systemd/system-preset/90-%{name}.preset

%changelog
%autochangelog
