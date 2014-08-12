#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Bonjour
Summary:	Net::Bonjour - Module for DNS service discovery (Apple's Bonjour)
Summary(pl.UTF-8):	Net::Bonjour - moduł dla wykrywania usług za pomocą DNS (Apple Bonjour)
Name:		perl-Net-Bonjour
Version:	0.96
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	619e15831c8db014ceff422191fe6538
URL:		http://search.cpan.org/dist/Net-Bonjour/
Patch0:		%{name}-prompt.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS >= 0.5
%endif
Provides:	perl-Net-Rendezvous
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Bonjour is a set of modules that allow one to discover local
services via multicast DNS (mDNS) or enterprise services via
traditional DNS. This method of service discovery has been branded as
Bonjour by Apple Computer.

The base object would be of the Net::Bonjour class. This object
contains the resolver for DNS service discovery.

The base object (Net::Bonjour) will return entry objects of the class
Net::Bonjour::Entry.

%description -l pl.UTF-8
Net::Bonjour - moduł dla wykrywania usług za pomocą DNS (Apple
Bonjour)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/*.pm
%dir %{perl_vendorlib}/Net/Bonjour
%dir %{perl_vendorlib}/Net/Rendezvous
%{perl_vendorlib}/Net/Bonjour/*.pm
%{perl_vendorlib}/Net/Rendezvous/Entry.pm
%{_mandir}/man3/*
