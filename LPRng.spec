Summary:	A next-generation printing system for UNIX
Name:		LPRng
Version:	3.5.3
Release:	1
Copyright:	GPL
Group:		Utilities/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	ftp://ftp.astart.com/pub/LPRng/LPRng/%{name}_DOC-%{version}.tgz
Source2:	lpd.init
Requires:	/sbin/chkconfig
BuildRoot:	/tmp/%{name}-%{version}-root
Provides:	lpr
Obsoletes:	lpr

%description
LPRng is the "next generation" printing system for UNIX, featuring
enhanced reliability and security.

%prep
%setup -q
# %setup -a1 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr 
#	--with-lpddir=/usr/sbin \
#	--with-admindir=/usr/sbin

make

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT/etc/rc.d/init.d

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	INSTALL_LIB=$RPM_BUILD_ROOT/usr/sbin \
	INSTALL_MAINT=$RPM_BUILD_ROOT/usr/sbin \
	SUID_ROOT_PERMS="755"

install $RPM_SOURCE_DIR/lpd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
install lpd.conf lpd.perms $RPM_BUILD_ROOT/etc
# /etc/printcap is in the setup package
# touch $RPM_BUILD_ROOT/etc/printcap

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
%defattr(644, root, root, 755)
# /etc/printcap is in the setup package
# %config /etc/printcap
%config /etc/lpd.conf
%config /etc/lpd.perms
%doc ABOUT-NLS.LPRng ANNOUNCE Artistic.license CHANGES CONTRIBUTORS
%doc Commercial.license HOWTO INSTALL LICENSE README* TESTSUPPORT
%attr(755,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/*
%attr(644,root, man) /usr/man/man[158]/*

%changelog
* Tue Dec  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
