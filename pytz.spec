%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pytz
Version:        2010h
Release:        2%{?dist}
Summary:        World Timezone Definitions for Python

Group:          Development/Languages
License:        MIT
URL:            http://pytz.sourceforge.net/
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         pytz-2010h_zoneinfo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

Requires: tzdata

%description
pytz brings the Olson tz database into Python. This library allows accurate
and cross platform timezone calculations using Python 2.3 or higher. It
also solves the issue of ambiguous times at the end of daylight savings,
which you can read more about in the Python Library Reference
(datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/pytz/*.py
rm -rf  $RPM_BUILD_ROOT%{python_sitelib}/pytz/zoneinfo

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt README.txt
%{python_sitelib}/pytz/
%{python_sitelib}/*.egg-info

%changelog
* Wed Jun 30 2010 David Malcolm <dmalcolm@redhat.com> - 2010h-2
- rebuild

* Wed Jun 30 2010 David Malcolm <dmalcolm@redhat.com> - 2010h-1
- 2010h
- use %%global rather than %%define

* Fri Jan 29 2010 David Malcolm <dmalcolm@redhat.com> - 2008i-6.2
- fix source URL

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2008i-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008i-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008i-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2008i-4
- Rebuild for Python 2.6

* Tue Nov 18 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-3
- Apply patch correctly.

* Thu Nov 13 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-2
- Updated tzdata patch from Petr Machata bug 471014

* Tue Nov 11 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-1
- Update to latest, now using timezone files provided by tzdata package

* Fri Jan 04 2008 Jef Spaleta <jspaleta@gmail.com> 2006p-3
- Fix for egg-info file creation

* Mon Dec 11 2006 Jef Spaleta <jspaleta@gmail.com> 2006p-2
- Bump for rebuild against python 2.5 and change BR to python-devel accordingly

* Fri Dec  8 2006 Orion Poplawski <orion@cora.nwra.com> 2006p-1
- Update to 2006p

* Thu Sep  7 2006 Orion Poplawski <orion@cora.nwra.com> 2006g-1
- Update to 2006g

* Mon Feb 13 2006 Orion Poplawski <orion@cora.nwra.com> 2005r-2
- Rebuild for gcc/glibc changes

* Tue Jan  3 2006 Orion Poplawski <orion@cora.nwra.com> 2005r-1
- Update to 2005r

* Thu Dec 22 2005 Orion Poplawski <orion@cora.nwra.com> 2005m-1
- Update to 2005m

* Fri Jul 22 2005 Orion Poplawski <orion@cora.nwra.com> 2005i-2
- Remove -O1 from install command

* Tue Jul 05 2005 Orion Poplawski <orion@cora.nwra.com> 2005i-1
- Initial Fedora Extras package
