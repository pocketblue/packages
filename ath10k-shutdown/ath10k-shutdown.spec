Name:             ath10k-shutdown
Version:          1
Release:          0%{?dist}
Summary:          disable ath10k modules on shutdown
License:          AGPL-3.0
URL:              https://github.com/pocketblue/packages
Source0:          ath10k-shutdown.service
Source1:          90-ath10k-shutdown.preset
BuildArch:        noarch
Requires(post):   systemd
Requires(postun): systemd
BuildRequires:    systemd-rpm-macros
%{?systemd_requires}

%description
ensure that ath10k modules are disabled before shutdown, required for proper shutdown process on oneplus6 and mipad5

%install
install -Dm0644 %{SOURCE0} %{buildroot}%{_unitdir}/ath10k-shutdown.service
install -Dm0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/90-ath10k-shutdown.preset

%post
%systemd_post                ath10k-shutdown.service
%preun
%systemd_preun               ath10k-shutdown.service
%postun
%systemd_postun_with_restart ath10k-shutdown.service

%files
%{_unitdir}/ath10k-shutdown.service
%{_prefix}/lib/systemd/system-preset/90-ath10k-shutdown.preset

%changelog
* Tue Sep 30 2025 gmanka
- init
