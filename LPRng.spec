Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Name:		LPRng
Version:	3.7.3
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	%{name}.init
Source2:	%{name}.conf
Patch0:		%{name}-filter.patch
Patch1:		%{name}-ac_fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
Requires:	/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
URL:		http://www.astart.com/lprng/LPRng.html
Provides:	lpr
Obsoletes:	lpr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The LPRng software is an enhanced, extended, and portable
implementation of the Berkeley LPR print spooler functionality. While
providing the same interface and meeting RFC1179 requirements, the
implementation is completely new and provides support for the
following features: lightweight (no databases needed) lpr, lpc, and
lprm programs; dynamic redirection of print queues; automatic job
holding; highly verbose diagnostics; multiple printers serving a
single queue; client programs do not need to run SUID root; greatly
enhanced security checks; and a greatly improved permission and
authorization mechanism.

The source software compiles and runs on a wide variety of UNIX
systems, and is compatible with other print spoolers and network
printers that use the LPR interface and meet RFC1179 requirements.
LPRng provides emulation packages for the SVR4 lp and lpstat programs,
eliminating the need for another print spooler package. These
emulation packages can be modified according to local requirements, in
order to support vintage printing systems.

For users that require secure and/or authenticated printing support,
LPRng supports Kerberos V, MIT Kerberos IV Print Support, and PGP
authentication. LPRng is being adopted by MIT for use as their Campus
Wide printing support system. Additional authentication support is
extremely simple to add. LPRng is Open Source Software, and the
current public distribution is available from the listed FTP and Web
Sites.

%description -l pl
LPRng jest systemem drukowania nowej generacji zwiêkszaj±cym
niezawodno¶æ i bezpieczeñstwo.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
aclocal
autoconf
%configure \
	--disable-setuid \
	--with-userid=lp \
	--with-groupid=lp \
	--with-filterdir=%{_libdir}/lpfilters \
	--with-lockfile=%{_var}/spool/lpd/lpd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_var}/spool/lpd}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
# yes, overwrite distribution lpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lpd.conf
install printcap $RPM_BUILD_ROOT%{_sysconfdir}/
install lpd.perms $RPM_BUILD_ROOT%{_sysconfdir}/

rm -fr TESTSUPPORT/{Makefile*,LPD}
mv -f lpd.conf TESTSUPPORT/lpd.conf.distrib

gzip -9nf CHANGES CONTRIBUTORS README* TESTSUPPORT/*

%find_lang %{name}

%post
/sbin/chkconfig --add lpd
if [ -f /var/lock/subsys/lpd ]; then
	/etc/rc.d/init.d/lpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/lpd start\" to start LPRng lpd daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/lpd ]; then
		/etc/rc.d/init.d/lpd stop 1>&2
	fi
	/sbin/chkconfig --del lpd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lpd.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lpd.perms
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/printcap
%doc {CHANGES,CONTRIBUTORS,README*}.gz TESTSUPPORT HOWTO/LPRng-HOWTO.html
%attr(754,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_libdir}/lpfilters
%attr(755,root,root) %{_libdir}/lpfilters/*
%dir %attr(750,root,lp) %{_var}/spool/lpd
%{_mandir}/man[158]/*
