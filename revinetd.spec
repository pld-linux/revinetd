Summary:	revinetd - reverse data port forwarder
Summary(pl.UTF-8):   revinetd - narzędzie do odwrotnego przekierowywania portów
Name:		revinetd
Version:	1.0.1
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/revinetd/%{name}-%{version}.tar.gz
# Source0-md5:	b04af5730498fa3e625a52c5fb79816b
URL:		http://revinetd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Revinetd is a GNU implementation of the TCP gender changer. It
operates in two modes, listen-listen and connect-connect. It can be
used to forward traffic through firewalls where outbound rule sets are
more liberal than inbound rules.

%description -l pl.UTF-8
Revinetd to implementacja GNU zmieniacza rodzaju TCP. Działa w dwóch
trybach: słuchania-słuchania i łączenia-łączenia. Może być używany do
przekierowywania ruchu poprzez firewalle, gdzie zestawy reguł dla
połączeń wychodzących są bardziej liberalne niż dla połączeń
przychodzących.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
