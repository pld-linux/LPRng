Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Name:		LPRng
Version:	3.6.8
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	lpd.init
Patch0:		LPRng-autoconf.patch
Requires:	/sbin/chkconfig
URL:		http://www.astart.com/lprng/LPRng.html
Provides:	lpr
Obsoletes:	lpr
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_libdir	%{_sbindir}

%description
The LPRng software is an enhanced, extended, and portable implementation of
the Berkeley LPR print spooler functionality. While providing the same
interface and meeting RFC1179 requirements, the implementation is completely
new and provides support for the following features: lightweight (no
databases needed) lpr, lpc, and lprm programs; dynamic redirection of print
queues; automatic job holding; highly verbose diagnostics; multiple printers
serving a single queue; client programs do not need to run SUID root;
greatly enhanced security checks; and a greatly improved permission and
authorization mechanism.

The source software compiles and runs on a wide variety of UNIX systems, and
is compatible with other print spoolers and network printers that use the
LPR interface and meet RFC1179 requirements.  LPRng provides emulation
packages for the SVR4 lp and lpstat programs, eliminating the need for
another print spooler package. These emulation packages can be modified
according to local requirements, in order to support vintage printing
systems.

For users that require secure and/or authenticated printing support, LPRng
supports Kerberos V, MIT Kerberos IV Print Support, and PGP authentication. 
LPRng is being adopted by MIT for use as their Campus Wide printing support
system. Additional authentication support is extremely simple to add.  LPRng
is Open Source Software, and the current public distribution is available
from the listed FTP and Web Sites.

%description -l pl
LPRng jest systemem drukowania nowej generacji zwiêkszaj±cym niezawodno¶æ 
i bezpieczeñstwo.

%prep
%setup  -q
%patch0 -p1

%build
gettextize --copy --force
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-nls \
	--disable-setuid \
	--without-included-gettext

make

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT/etc/rc.d/init.d

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	LPD_CONF_PATH=$RPM_BUILD_ROOT/etc/lpd.conf \
	LPD_PERMS_PATH=$RPM_BUILD_ROOT/etc/lpd.perms

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd

rm -fr TESTSUPPORT/{Makefile*,LPD}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ANNOUNCE CHANGES CONTRIBUTORS \
	README* TESTSUPPORT/* HOWTO/LPRng-HOWTO.txt

%find_lang %{name}

%post
/sbin/chkconfig --add lpd
if test -r /var/run/lpd.pid; then
	/etc/rc.d/init.d/lpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/lpd start\" to start mcserv daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del lpd
	/etc/rc.d/init.d/lpd stop 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) /etc/lpd.conf
%config(noreplace) /etc/lpd.perms
%doc {ANNOUNCE,CHANGES,CONTRIBUTORS}.gz
%doc {HOWTO/LPRng-HOWTO.txt,README*}.gz TESTSUPPORT
%attr(754,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_libexecdir}/filters
%attr(755,root,root) %{_libexecdir}/filters/*
%{_mandir}/man[158]/*
