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
Release:       %mkrel 13
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
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-11mdv2011.0
+ Revision: 662869
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-10mdv2011.0
+ Revision: 603462
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-9mdv2010.1
+ Revision: 518963
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-8mdv2010.0
+ Revision: 413105
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.51.0-7mdv2009.1
+ Revision: 350118
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.51.0-6mdv2009.0
+ Revision: 220446
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.51.0-5mdv2008.1
+ Revision: 182655
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.51.0-4mdv2008.1
+ Revision: 148854
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-3mdv2007.0
+ Revision: 123368
- Import aspell-sv

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.51.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.51.0-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.51.0-1mdk
- updated to 0.51.0

