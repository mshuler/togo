Summary: Set of Scripts to Assist with RPM Building
Name: togo
Version: 1.1
Release: 4
License: GNU GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRoot: %{_tmppath}/%{name}
#Typically, prefix should be set to /usr
Prefix: /usr/local
#Man pages directory
%define man_dir %{prefix}/share/man/man1
#Scripts/executables directory
%define exe_dir %{prefix}/bin
#Template/additional info directory
%define template_dir %{prefix}/share/doc/%{name}
#Until there is a config file, don't do this
##Configuration files directory
#%define conf_dir %{prefix}/etc

#These examples provide proper dependency information for this package.
Requires: bash
Requires: rpm-build
Requires: perl

#Explicitly turn off the debuging for package to save some build time.
%define debug_package %{nil}

%description
Togo is a set of scripts to assist with the 
building of RPMS.

%prep
rm -rf %{buildroot}
%setup -q -c -a 0

%build

%install
cp -R root/* %{buildroot}

%clean
rm -fr %{buildroot}

%files
%defattr(755,root,root)
%{exe_dir}/togomake
%{exe_dir}/togoprep
%{exe_dir}/togobuild
%{template_dir}/togo-spec.spec
%{template_dir}/togo-man.1
%doc %{man_dir}/togo.1*

%pre

%post

%preun

%postun

%changelog

* Mon Nov  6 2006 Gene Reese <gene.reese@xirsix.com>
- Modified togomake to exclude cleaning of usr/ directory unless it's empty
- Modified default archiver options of togomake

* Mon May 05 2006 Gene Reese <gene.reese@xirsix.com>
- Initial version.
