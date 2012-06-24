Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Summary(pt_BR):	Gerenciador de impress�o para UNIX e NT
Summary(ru):	������ ������ LPRng
Summary(uk):	������ ����� LPRng
Summary(zh_CN):	LPRng--��ӡ����
Name:		LPRng
Version:	3.8.28
Release:	3
License:	GPL or Artistic
Group:		Applications/System
Source0:	ftp://ftp.lprng.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
# Source0-md5:	1b3a0abd291b260eab6087ac0e61ed84
Source1:	%{name}.init
Source2:	%{name}.conf
Source3:	%{name}.printcap
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
# Source4-md5:	4771b1c3598677a8201a9e203235dff3
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-lpd-perms.patch
Patch2:		%{name}-ngettext.patch
Patch3:		%{name}-missing-nls.patch
Patch4:		%{name}-pl.po.patch
Patch5:		%{name}-types.patch
Patch6:		%{name}-shell.patch
URL:		http://www.lprng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.315
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Obsoletes:	cups
Obsoletes:	cups-clients
Obsoletes:	lpr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

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
LPRng jest rozszerzon�, ulepszon� i portowaln� implementacj�
Berkeleyowskiego LPR, czyli spoolera wydruk�w. Dostarcza ten sam
interfejs oraz jest zgodny z wymaganiami RFC1179. Jednocze�nie
wykonanie jest ca�kowicie nowe i dostarcza nast�puj�ce rzeczy:
- programy - "lekki" lpr (nie s� potrzebne �adne bazy danych), lpc,
  oraz lprm;
- dynamiczna redyrekcja do kolejek;
- automatyczne wstrzymywanie zada�;
- "gadatliwa" diagnostyka;
- obs�ug� wielu drukarek na jednej kolejce;
- programy klienckie nie musz� by� SUID root;
- mocno rozszerzona kontrola bezpiecze�stwa;
- mocno rozszerzone mechanizmy bezpiecze�stwa i kontroli uprawnie�.

Oprogramowanie to kompiluje si� i dzia�a na wielu systemach uniksowych
i jest kompatybilne z innymi print spoolami oraz drukarkami
sieciowymi, kt�re u�ywaj� interfejsu LPR oraz spe�niaj� wymagania
RFC1179. LPRng dostarcza pakiety emulacyjne dla program�w SVR4 lp oraz
lpstat, eliminuj�c w ten spos�b konieczno�� posiadania jeszcze jednego
pakietu print spoola. Te pakiety mog� by� modyfikowane zgodnie z
lokalnymi wymaganiami.

Dla u�ytkownik�w, kt�rzy potrzebuj� bezpiecznej i uwierzytelnianej
obs�ugi drukowania LPRng wspiera Kerberos V, MIT Kerberos IV Print
Support oraz PGP.

%description -l pt_BR
LPRng � uma vers�o melhorada, estendida e mais segura do gerenciador
de impress�o LPR. Entre as melhorias se destacam: redirecionamento
din�mico de filas de impress�o, suspens�o autom�tica de trabalhos de
impress�o, diagn�stico detalhado, v�rias impressoras por fila,
programas cliente n�o precisam ser SUID root e um mecanismo bastante
melhorado de permiss�es e autoriza��es.

%description -l ru
LPRng - ��� ����������, ����������� � ����������� ����������
���������������� ������� ������ Berkeley LPR. ������������ ��� ��
��������� � ������� ���� ����������� RFC1179, ��� ����������
���������� ����� � ������������� ��������� ��������� ������������:
���������� (�� ��������� ���� ������) lpr, ��������� lpc � lprm;
������������ ������������� �������� ������; ��������������
������������ �������; ����� ��������� �����������; ������������ �����
������� ����������� ����������; ���������� ��������� �� ������ ����
SUID root; ������ ���������� ������� ������������; ������ ����������
��������� ����������� � ���� �������.

����������� ����������� �������������� � �������� �� �������
���������� UNIX-������ � ���������� � ������� ��������� ������ �
�������� ����������, ������� ���������� ��������� LPR � ��������
����������� RFC1179. LPRng ����� ������������� ������ �������� ���
�������� SVR4 lp � lpstat, �������� ����������� � ������ ������
������� ������. ��� ������ �������� ����� ���� �������������� �
������������ � ���������� ������������ ��� ��������� �����������
������ ������.

��� �������������, ������� ����� ���������� �/��� ���������������
��������� ������, LPRng ������������ Kerberos V, MIT Kerberos IV Print
Support � ������������ PGP. LPRng ������ �� �������� � MIT ���
������������� � �������� ������� ��������� ������ � �� �������.
�������������� ��������� ������������ ����� ���� ��������� ��� ������
������.

%description -l uk
LPRng - �� ���������, ��������� �� ��������� ���̦��æ� ����æ����Ԧ
������� ����� Berkeley LPR. ������� ��� �� ��������� �� צ���צ�����
�Ӧ� ������� RFC1179, �� ���̦��æ� ��������� ���� � ����� Ц�������
����� �����������: ���������� (�� ���������� ���� �����) lpr, ��������
lpc �� lprm; ����ͦ��� ����������æ� ���� �����; �����������
������������ �������; ���� �������� Ħ���������; �������������� ���ϧ
����� ˦������ �Ҧ�������; �̦�����˦ �������� �� �����Φ ���� SUID
root; ������ ��������� ������� �������; ������ �������Φ ����Φ���
��������æ� �� ���� �������.

��������� ������������ ���Ц������� �� ������ �� ����˦� ˦�����Ԧ
UNIX-������ � ��ͦ��� � ������ ��������� ����� �� ����������
�Ҧ�������, ���Ҧ �������������� ��������� LPR �� צ���צ����� �������
RFC1179. LPRng ����� ����� ������ �����æ� ��� ������� SVR4 lp ��
lpstat, ���������� ������� � ������ ����Ԧ ������� �����. � ������
�������� ������ ���� ����Ʀ����Φ � צ���צ����Ԧ � ����������
�������� ��� Ц������� ����������� ������ �����.

��� ���������ަ�, ���� ���Ҧ��� �������� ��/��� �������Ʀ������
Ц������� �����, LPRng Ц�����դ Kerberos V, MIT Kerberos IV Print
Support �� ���������æ� PGP. LPRng �������� �� �������� � MIT ���
������������ � ����Ԧ ������� Ц������� ����� � �� �����Ӧ. ���������
Ц������� ���������æ� ���� ���� ������ ��� ��������� ������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

rm -rf autom4te.cache
mv  PrintingCookbook/{HTML,PrintingCookbook}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/{config.*,missing} .
# now it wants to use /etc/lpd/lpd.{conf,perms} - stick to old values?
%configure \
	OPENSSL=/usr/bin/openssl \
	PSHOWALL="-ax" \
	--disable-setuid \
	--enable-shared \
	--with-userid=lp \
	--with-groupid=lp \
	--with-filterdir=%{_libdir}/lpfilters \
	--with-lockfile=%{_var}/spool/lpd/lpd \
	--with-lpd_conf_path=%{_sysconfdir}/lpd.conf \
	--with-lpd_perms_path=%{_sysconfdir}/lpd.perms \
	--with-done_jobs=0 \
	--disable-werror

%{__make} -j1
%{__make} -C man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_var}/spool/lpd/lp} \
	$RPM_BUILD_ROOT%{_sysconfdir}/lpd/ssl.{ca,crl,server}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	POSTINSTALL="NO"
%{__make} install -C man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
# yes, overwrite distribution lpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lpd.conf
echo "default_printer = lp" >> $RPM_BUILD_ROOT%{_sysconfdir}/lpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/printcap
install lpd.perms $RPM_BUILD_ROOT%{_sysconfdir}

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_libdir}/liblpr.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add lpd
%service lpd restart "LPRng lpd daemon"

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del lpd
	%service lpd stop
fi

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS COPYRIGHT README README.SSL* TODO
%doc DOCS/LPRng-Reference-Multipart PrintingCookbook/PrintingCookbook
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lpd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lpd.perms
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/printcap
%dir %{_sysconfdir}/lpd
# what perms?
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.ca
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.crl
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.server
%attr(754,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/lpfilters
%attr(755,root,root) %{_libdir}/lpfilters/*
%dir %attr(750,root,lp) %{_var}/spool/lpd
%dir %attr(770,root,lp) %{_var}/spool/lpd/lp
%{_mandir}/man[158]/*
%lang(pl) %{_mandir}/pl/man[158]/*
