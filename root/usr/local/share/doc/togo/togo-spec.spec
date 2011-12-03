
#########################################
# Helpful Path Variables
#    (These are already defined in /var/lib/rpm/macros)
#
# %_prefix           /usr
# %_exec_prefix      %{_prefix}
# %_bindir           %{_exec_prefix}/bin
# %_sbindir          %{_exec_prefix}/sbin
# %_libexecdir       %{_exec_prefix}/libexec
# %_datadir          %{_prefix}/share
# %_sysconfdir       %{_prefix}/etc
# %_sharedstatedi    %{_prefix}/com
# %_localstatedir    %{_prefix}/var
# %_lib	             lib
# %_libdir           %{_exec_prefix}/%{_lib}
# %_includedir       %{_prefix}/include
# %_oldincludedir    /usr/include
# %_infodir          %{_prefix}/info
# %_mandir           %{_prefix}/man

#########################################

Summary: This is an example summary
Name: example
Version: 1.0
Release: 1
License: GNU GPL
Group: Applications
Source0: %{name}-%{version}.tar
BuildArch: noarch

BuildRoot: %{_tmppath}/%{name}

# These examples provide proper dependency information for this package.
#Requires: 

# Explicitly turn off the debuging for package to save some build time.
%define debug_package %{nil}

%description
This is a an example description.

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
# By default, we include all files
/*

%pre

%post

%preun

%postun

%changelog
* Fri Dec 02 2011 Your Name <Your_Name@whatever.com>
- Initial version.
