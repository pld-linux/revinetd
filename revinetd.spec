Summary:	revinetd - reverse data port forwarder
Summary(pl):	revinetd - narzêdzie do odwrotnego przekierowywania portów
Name:		revinetd
Version:	0.9
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7a36393f22b26d57ab486700efb7dcda
URL:		http://revinetd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Revinetd is a GNU implementation of the TCP gender changer. It
operates in two modes, listen-listen and connect-connect. It can be
used to forward traffic through firewalls where outbound rule sets are
more liberal than inbound rules.

%description -l pl
Revinetd to implementacja GNU zmieniacza rodzaju TCP. Dzia³a w dwóch
trybach: s³uchania-s³uchania i ³±czenia-³±czenia. Mo¿e byæ u¿ywany do
przekierowywania ruchu poprzez firewalle, gdzie zestawy regu³ dla
po³±czeñ wychodz±cych s± bardziej liberalne ni¿ dla po³±czeñ
przychodz±cych.

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
