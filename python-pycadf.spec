# Created by pyp2rpm-1.0.1
%global sname pycadf

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        DMTF Cloud Audit (CADF) data model

License:        ASL 2.0
URL:            https://launchpad.net/pycadf
Source0:        https://pypi.io/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:      noarch


%description
DMTF Cloud Audit (CADF) data model


%package -n python2-%{sname}
Summary:        DMTF Cloud Audit (CADF) data model

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-debtcollector
Requires:       python-iso8601
Requires:       python-netaddr
Requires:       python-oslo-config
Requires:       python-oslo-messaging
Requires:       python-oslo-serialization
Requires:       pytz
Requires:       python-six >= 1.9.0
Requires:       python-webob >= 1.2.3
Requires:       python-%{sname}-common = %{version}-%{release}

%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
DMTF Cloud Audit (CADF) data model

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        DMTF Cloud Audit (CADF) data model

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3-babel
Requires:       python3-debtcollector
Requires:       python3-iso8601
Requires:       python3-netaddr
Requires:       python3-oslo-config
Requires:       python3-oslo-messaging
Requires:       python3-oslo-serialization
Requires:       python3-pytz
Requires:       python3-six >= 1.9.0
Requires:       python3-webob >= 1.2.3
Requires:       python-%{sname}-common = %{version}-%{release}

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
DMTF Cloud Audit (CADF) data model
%endif

%package -n python-%{sname}-common
Summary:        DMTF Cloud Audit (CADF) data model

%description -n python-%{sname}-common
DMTF Cloud Audit (CADF) data model (common data file)


%prep
%setup -q -n %{sname}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{sname}.egg-info


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/usr/etc/%{sname} %{buildroot}/%{_sysconfdir}/


%files -n python2-%{sname}
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}-%{upstream_version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-%{upstream_version}-py?.?.egg-info
%endif

%files -n python-%{sname}-common
%doc README.rst
%license LICENSE
%dir %{_sysconfdir}/%{sname}
%config(noreplace) %{_sysconfdir}/%{sname}/*.conf


%changelog
