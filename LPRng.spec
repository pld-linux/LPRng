Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Name:		LPRng
Version:	3.6.2
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	lpd.init
Patch0:		LPRng-install.patch
Patch1:		LPRng-autoconf.patch
Requires:	/sbin/chkconfig
URL:		http://www.astart.com/lprng/LPRng.html
Provides:	lpr
Obsoletes:	lpr
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_libdir	%{_sbindir}

%description
LPRng is the "next generation" printing system for UNIX, featuring
enhanced reliability and security.

%description -l pl
LPRng jest systemem drukowania nowej generacji zwiêkszaj±cym niezawodno¶æ 
i bezpieczeñstwo.

%prep
%setup  -q
%patch0 -p0
%patch1 -p1

%build
gettextize --copy --force
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-nls \
	--with-included-gettext

make

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT/etc/rc.d/init.d

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	LPD_CONF_PATH=$RPM_BUILD_ROOT/etc/lpd.conf \
	LPD_PERMS_PATH=$RPM_BUILD_ROOT/etc/lpd.perms \
	SUID_ROOT_PERMS="755"

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
%{_mandir}/man[158]/*
