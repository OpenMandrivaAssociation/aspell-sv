%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.51-0
%define languagelocal svenska
%define languageeng swedish
%define languageenglazy Swedish
%define languagecode sv

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.51.0
Release:       %mkrel 4
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:       LGPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary

# RedHat Stuff. is this right:
#Obsoletes: ispell-se, ispell-swedish, aspell-se

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv README README.%{languagecode}
chmod 644 README* Copyright doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*


