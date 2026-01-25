%global _commit 1b102ba5126bbbdae0efa6f568ac2467392b49f4
Name:           qca-swiss-army-knife
Version:        2022.07.01
Release:        %autorelease
Summary:        Utilities to help and debug Qualcomm Atheros wireless driver development
License:        ICS
URL:            https://github.com/qca/qca-swiss-army-knife
Source0:        %{url}/archive/%{_commit}.tar.gz

Requires:       python3

%description
%{summary}

%prep
tar -xzf %{SOURCE0}

%build

%install
cd %{name}-%{_commit}
find tools/scripts -type f -exec install -Dm755 {} -t %{buildroot}/usr/bin \;
install -d %{buildroot}/usr/share/licenses/qca-swiss-army-knife/
install -Dm644 LICENSE %{buildroot}/usr/share/licenses/qca-swiss-army-knife/

%files
%license LICENSE
/usr/bin/*

%changelog
%autochangelog
