%global debug_package %{nil}
%global buildforkernels akmod

%global modname  idtp9418
%global commit   eaa2719e71f5ad762250e0705fb13f38f8856cfc

Name:           %{modname}-kmod
Version:        0.1
Release:        %autorelease
Summary:        idtp9418 wireless charger driver
License:        GPL-2.0-only
URL:            https://github.com/nik012003/idtp9418-mainline
Source0:        %{url}/archive/eaa2719e71f5ad762250e0705fb13f38f8856cfc.tar.gz

BuildRequires: kmodtool

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{modname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null)}


%description
%{summary}


%package       common
Summary:       Common files for the %{modname} kernel module
BuildArch:     noarch
Provides:      %{modname}-kmod-common = %{version}-%{release}

%description   common
%{summary}

%files         common


%prep
%{?kmodtool_check}

kmodtool --target %{_target_cpu} --kmodname %{modname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    cp -a %{modname}-mainline-%{commit} _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done

%{?akmod_install}


%files
# filled by kmodtool


%changelog
%autochangelog
