%global commit d93ae53320ff866d55cb9be64afc10592e760c1c

Name:           sdm845-fwload
Version:        0.1
Release:        %autorelease
Summary:        A tool to extract firmware from a running SDM845 device

License:        MIT
URL:            https://github.com/pocketblue/sdm845-fwload
Source:         %{url}/archive/%{commit}.tar.gz

BuildRequires:  systemd-rpm-macros
Requires:       pil-squasher

%description
%{summary}.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{commit}

%install
install -Dm755 %{name} -t %{buildroot}%{_bindir}/
install -Dm644 %{name}.service -t %{buildroot}%{_unitdir}/

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
