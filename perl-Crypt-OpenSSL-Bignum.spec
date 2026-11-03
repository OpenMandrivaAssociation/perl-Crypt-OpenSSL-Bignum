%define upstream_name Crypt-OpenSSL-Bignum

Summary:	Perl interface to OpenSSL multiprecision integers
Name:		perl-%{upstream_name}
Version:	0.09
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Crypt::OpenSSL::Bignum
Source0:	https://cpan.metacpan.org/authors/id/K/KM/KMX/Crypt-OpenSSL-Bignum-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	pkgconfig(openssl)
BuildRequires:	perl-devel
BuildRequires:	perl(Test)

%description
Perl interface to OpenSSL's multiprecision integer arithmetic.
Crypt::OpenSSL::RSA needs this module.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/man3/*
