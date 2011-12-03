
#########################################
# RPM documentation may be found here:
#  http://www.rpm.org/max-rpm/
#
# Specifically, chapter 13: Inside the Spec File
#  http://www.rpm.org/max-rpm/ch-rpm-inside.html
#########################################

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

# The summary of the RPM
Summary: This is an example summary

# The name of the RPM
Name: example

# The version of the RPM
Version: 1.0

# The release number for this version
Release: 1

# The license information
License: GNU GPL

# What group should this RPM be associated with
Group: Applications

# The main source of the RPM. You may set the compression type by changing
#  the file extension. The scripts will attempt to build based on what
#  extension they find here
#
# Set the file extension of the source to any of these three choices:
#  .tar     - Create an RPM using no compression
#  .tar.gz  - Create an RPM using gzip compression
#  .tar.bz2 - Create an RPM using bzip compression
Source0: %{name}-%{version}.tar.gz

# Define the build architecture for this RPM
#  noarch, i386, x86_64, etc.
BuildArch: noarch

# Don't change this
BuildRoot: %{_tmppath}/%{name}

# These examples provide proper dependency information for this package.
#Requires: bash, python >= 2.7

# Explicitly turn off the debuging for package to save some build time.
%define debug_package %{nil}

# The description of this RPM
%description
This is a an example description.

# More information about the following sections may be found here:
#  http://www.rpm.org/max-rpm/s1-rpm-inside-scripts.html
%prep
rm -rf %{buildroot}
# Information regarding the %setup macro may be found here:
#  http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
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
