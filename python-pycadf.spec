# Created by pyp2rpm-1.0.1
%global pypi_name pycadf

# see https://fedoraproject.org/wiki/Packaging:Python#Macros
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        DMTF Cloud Audit (CADF) data model

License:        ASL 2.0
URL:            https://launchpad.net/pycadf
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-iso8601
Requires:       python-netaddr
Requires:       python-oslo-config >= 1:1.9.3
Requires:       python-oslo-context
Requires:       python-oslo-i18n
Requires:       python-oslo-messaging >= 1.4.0.0
Requires:       python-oslo-serialization
Requires:       python-posix_ipc
Requires:       pytz
Requires:       python-six >= 1.9.0
Requires:       python-webob >= 1.2.3

%description
DMTF Cloud Audit (CADF) data model

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/usr/etc/%{pypi_name} %{buildroot}/%{_sysconfdir}/
rm -rf %{buildroot}/%{python_sitelib}/%{pypi_name}/tests


%files
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/%{pypi_name}
%config(noreplace) %{_sysconfdir}/%{pypi_name}/*.conf
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue Mar 31 2015 Alan Pevec <apevec@redhat.com> - 0.8.0-1
- new version

* Wed Sep 17 2014 Alan Pevec <apevec@redhat.com> - 0.6.0-2
- update dependencies

* Sat Sep 06 2014 Pádraig Brady <pbrady@redhat.com> - 0.6.0-1
- Latest upstream

* Fri Jun 13 2014 Pádraig Brady <pbrady@redhat.com> - 0.5.1-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Lon Hohberger <lhh@redhat.com> - 0.4.1-3
- Add python-setuptools build requirement

* Fri Mar 07 2014 Padraig Brady <P@draigBrady.com> - 0.4.1-2
- Initial package.
