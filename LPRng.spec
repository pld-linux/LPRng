Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Name:		LPRng
Version:	3.5.4
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzędzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}_DOC-3.5.3.tgz
Source2:	lpd.init
Requires:	/sbin/chkconfig
URL:		http://www.astart.com/lprng/LPRng.html
Provides:	lpr
Obsoletes:	lpr
BuildRoot:	/tmp/%{name}-%{version}-root

%description
LPRng is the "next generation" printing system for UNIX, featuring
enhanced reliability and security.

%description -l pl
LPRng jest systemem drukowania nowej generacji zwiększającym niezawodność 
i bezpieczeństwo.

%prep
%setup -q
# %setup -a1 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr 
#	--with-lpddir=%{_sbindir} \
#	--with-admindir=%{_sbindir}

make

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT/etc/rc.d/init.d

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_sbindir} \
	INSTALL_MAINT=$RPM_BUILD_ROOT%{_sbindir} \
	SUID_ROOT_PERMS="755"

install $RPM_SOURCE_DIR/lpd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
install lpd.conf lpd.perms $RPM_BUILD_ROOT/etc
# /etc/printcap is in the setup package
# touch $RPM_BUILD_ROOT/etc/printcap

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ANNOUNCE Artistic.license CHANGES CONTRIBUTORS \
	Commercial.license HOWTO README* TESTSUPPORT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if test -r /etc/rc.d/init.d/lpd
	then /etc/rc.d/init.d/lpd stop
fi

if test -r /etc/rc.d/init.d/lpd.init
	then /etc/rc.d/init.d/lpd.init stop
fi

%post
test "$1" = 1 && /sbin/chkconfig lpd on

%preun
if test "$1" = 0
then
	/etc/rc.d/init.d/lpd stop
	/sbin/chkconfig lpd off
fi

%files
%defattr(644,root,root,755)
# /etc/printcap is in the setup package
# %config /etc/printcap
%config /etc/lpd.conf
%config /etc/lpd.perms
%doc {ANNOUNCE,Artistic.license,CHANGES,CONTRIBUTORS}.gz
%doc {Commercial.license,HOWTO,README*,TESTSUPPORT}.gz
%attr(755,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*

%changelog
* Tue Feb  9 1999 Michał Kuratczyk <kurkens@polbox.com>
  [3.5.3-2]
- added pl translations
- added Group(pl)
- added gzipping man pages and documentation

* Tue Dec  1 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [3.5.3-1]
- added -q %setup parameter,
- added gzipping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- removed INSTALL and COPYING from %doc,
- added using %%{name} and %%{version} in Source,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu Jan 29 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz
- Upgraded to 3.4.2
- Merged LPRng and LPRng-lpd packages - if you don't need lpd, chkconfig it off.
- Changed /etc/rc.d/init.d/lpd script to be chkconfig-compatible for RH5.0

* Thu Jun 5 1997 Timo Karjalainen <timok@iki.fi>
- Upgraded to version 3.2.6

* Sat May 31 1997 Timo Karjalainen <timok@iki.fi>
- Upgraded to version 3.2.5
- Some minor changes to specfile
