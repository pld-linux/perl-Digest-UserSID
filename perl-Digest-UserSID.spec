%define		pdir	Digest
%define		pnam	UserSID
Summary:	Digest::UserSID - managing of session IDs
Summary(pl.UTF-8):	Digest::UserSID - zarządzanie identyfikatorami sesji
Name:		perl-Digest-UserSID
Version:	1.05
Release:	5
# same as perl, but "free" in module header
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1d06119b1e0367823fb197a82b472fd4
URL:		http://search.cpan.org/dist/Digest-UserSID/
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::UserSID - Managing of Session IDs for Users on CGI- and
console-scripts.

%description -l pl.UTF-8
Moduł UserSID - zarządzający identyfikatorami sesji dla użytkowników w
skryptach CGI i konsolowych.

%prep
%setup -q -c

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Digest/UserSID.pm
%{_mandir}/man3/*
