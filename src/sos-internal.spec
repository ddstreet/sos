%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name sos-internal
%define version 1.8
%define release 0

Summary: SoS internal utilities for report analysis
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Group: Application/Tools

Source0: sos-%{version}.tar.gz
Source1: rhsupport.pub
Source2: rhsupport.key
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: https://hosted.fedoraproject.org/projects/sos

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%prep
tar xfz %{SOURCE0}

%install
rm -rf ${RPM_BUILD_ROOT}

cd sos-%{version}

install -D -m755 extras/sos-open ${RPM_BUILD_ROOT}/usr/bin/sos-open

install -D -m644 %{SOURCE1} ${RPM_BUILD_ROOT}/usr/share/sos/rhsupport.pub
install -D -m600 %{SOURCE2} ${RPM_BUILD_ROOT}/usr/share/sos/rhsupport.key

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
echo -n "Importing GPG keys... "
/usr/bin/gpg --import /usr/share/sos/rhsupport.pub &> /dev/null
/usr/bin/gpg --allow-secret-key-import --import /usr/share/sos/rhsupport.key &> /dev/null
echo "done."

%files
%defattr(-,root,root,-)
/usr/share/sos/rhsupport.pub
/usr/share/sos/rhsupport.key
/usr/bin/sos-open

%changelog
* Wed Sep  4 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.0
- the GPG key will be regenerated every time this package is built
