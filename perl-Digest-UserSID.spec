%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	UserSID
Summary:	Digest::UserSID Perl module - managing of Session IDs
Summary(pl):	Modu³ perla Digest::UserSID - zarz±dzanie identyfikatorami sesji
Name:		perl-Digest-UserSID
Version:	1.05
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::UserSID - Managing of Session IDs for Users on CGI- and
console-scripts. 
	  
%description -l pl
Modu³ UserSID - zarz±dzaj±cy identyfikatorami sesji dla u¿ytkowników w
skryptach CGI i konsolowych.

%prep
%setup -q -c

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Digest/UserSID.pm
%{_mandir}/man3/*
