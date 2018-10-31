%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.51-0
%define languagelocal svenska
%define languageeng swedish
%define languageenglazy Swedish
%define languagecode sv

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.51.0
Release:	22
Group:		System/Internationalization
License:	LGPLv2
Url:		http://aspell.net/
Source0:	ftp://ftp.gnu.org/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv README README.%{languagecode}
chmod 644 README* Copyright doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*

