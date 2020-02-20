# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
# Created by pyp2rpm-1.0.1
%global sname pycadf

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc DMTF Cloud Audit (CADF) data model


Name:           python-%{sname}
Version:        2.10.0
Release:        2%{?dist}
Summary:        DMTF Cloud Audit (CADF) data model

License:        ASL 2.0
URL:            https://launchpad.net/pycadf
Source0:        https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz
BuildArch:      noarch


%description
%{common_desc}


%package -n python%{pyver}-%{sname}
Summary:        DMTF Cloud Audit (CADF) data model
%{?python_provide:%python_provide python%{pyver}-%{sname}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

Requires:       python%{pyver}-debtcollector >= 1.2.0
Requires:       python%{pyver}-oslo-config >= 2:5.2.0
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-pytz
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python-%{sname}-common = %{version}-%{release}

%description -n python%{pyver}-%{sname}
%{common_desc}

%package -n python-%{sname}-common
Summary:        DMTF Cloud Audit (CADF) data model
%{?python_provide:%python_provide python-%{sname}-common}

%description -n python-%{sname}-common
%{common_desc}


%prep
%setup -q -n %{sname}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{sname}.egg-info


%build
%{pyver_build}


%install
%{pyver_install}

mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/usr/etc/%{sname} %{buildroot}/%{_sysconfdir}/


%files -n python%{pyver}-%{sname}
%{pyver_sitelib}/%{sname}
%{pyver_sitelib}/%{sname}-%{upstream_version}-py?.?.egg-info

%files -n python-%{sname}-common
%doc README.rst
%license LICENSE
%dir %{_sysconfdir}/%{sname}
%config(noreplace) %{_sysconfdir}/%{sname}/*.conf


%changelog
* Thu Oct 03 2019 Joel Capitao <jcapitao@redhat.com> 2.10.0-2
- Removed python2 subpackages in no el7 distros

* Wed Sep 18 2019 RDO <dev@lists.rdoproject.org> 2.10.0-1
- Update to 2.10.0

