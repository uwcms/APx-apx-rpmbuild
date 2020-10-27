%define name apx-rpmbuild

Name:           %{name}
Version:        %{version_rpm_spec_version}
Release:        %{version_rpm_spec_release}%{?dist}
Summary:        A helpful wrapper for rpmbuild automating package versioning from git.

License:        Reserved
URL:            https://github.com/uwcms/APx-%{name}
Source0:        %{name}-%{version_rpm_spec_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3 python-rpm-macros python3-rpm-macros python3-setuptools
Requires:       python3 rpm-build rpm-sign

%global debug_package %{nil}

%description
A helpful wrapper for rpmbuild automating package versioning from git.


%prep
%autosetup -n %{name}-%{version}


%build
export %{version_shellvars}
%py3_build


%install
export %{version_shellvars}
%py3_install


%files
%doc README.md
%{python3_sitelib}/*
%{_bindir}/apx-rpmbuild


%changelog
* Tue Oct 27 2020 Jesra Tikalsky <jtikalsky@hep.wisc.edu>
- Initial spec file
