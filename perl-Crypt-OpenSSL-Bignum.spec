%define upstream_name	 Crypt-OpenSSL-Bignum
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	9
Summary:	%{upstream_name} module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A Perl interface to OpenSSL's multiprecision integer arithmetic libraries.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-6
+ Revision: 680860
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-5mdv2011.0
+ Revision: 555715
- rebuild

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 0.40.0-4mdv2010.1
+ Revision: 534173
- rebuild

* Fri Sep 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-3mdv2010.0
+ Revision: 430532
- new perl version macro
- use standard optimisations
- spec cleanup

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - force rebuild
    - rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.04-4mdv2009.0
+ Revision: 256271
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2008.1
+ Revision: 152035
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 46616
- update to new version 0.04

  + Olivier Thauvin <nanardon@mandriva.org>
    - rebuild
    - rebuild


* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.03-3mdk
- Rebuild

* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.03-2mdk
- Rebuild for new perl. Update description.

* Mon Jun 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.03-1mdk
- Initial cooker release, introduced for perl-Net-DNS-SEC

