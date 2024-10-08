#
# Conditional build:
%bcond_with	kerberos5	# build with kerberos5 support
#
Summary:	A next-generation printing system for UNIX
Summary(pl.UTF-8):	System drukowania nowej generacji
Summary(pt_BR.UTF-8):	Gerenciador de impressão para UNIX e NT
Summary(ru.UTF-8):	Спулер печати LPRng
Summary(uk.UTF-8):	Спулер друку LPRng
Summary(zh_CN.UTF-8):	LPRng--打印程序
Name:		LPRng
Version:	3.9.0
Release:	1
License:	GPL v2 with OpenSSL exception or Artistic
Group:		Applications/System
# lprng.com seems dead now (2024)
#Source0:	http://www.lprng.com/DISTRIB/LPRng/%{name}-%{version}.tgz
Source0:	https://downloads.sourceforge.net/lprng/lprng-%{version}.tar.gz
# Source0-md5:	10f4ec823df0e021404284037138aa8a
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
# Source1-md5:	4771b1c3598677a8201a9e203235dff3
Source2:	%{name}.init
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-lpd-perms.patch
Patch2:		%{name}-libwrap.patch
Patch3:		%{name}-missing-nls.patch
Patch4:		%{name}-pl.po.patch
Patch5:		%{name}-types.patch
Patch8:		%{name}-lpd.conf.patch
Patch10:	%{name}-openssl1.1.patch
#URL:		http://www.lprng.com/
URL:		https://lprng.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.315
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Provides:	printingclient
Provides:	printingdaemon
Obsoletes:	printingclient
Obsoletes:	printingdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		lpfiltersdir	%{_libexecdir}/lpfilters

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

%description -l pl.UTF-8
LPRng jest rozszerzoną, ulepszoną i portowalną implementacją
Berkeleyowskiego LPR, czyli spoolera wydruków. Dostarcza ten sam
interfejs oraz jest zgodny z wymaganiami RFC1179. Jednocześnie
wykonanie jest całkowicie nowe i dostarcza następujące rzeczy:
- programy - "lekki" lpr (nie są potrzebne żadne bazy danych), lpc,
  oraz lprm;
- dynamiczna redyrekcja do kolejek;
- automatyczne wstrzymywanie zadań;
- "gadatliwa" diagnostyka;
- obsługę wielu drukarek na jednej kolejce;
- programy klienckie nie muszą być SUID root;
- mocno rozszerzona kontrola bezpieczeństwa;
- mocno rozszerzone mechanizmy bezpieczeństwa i kontroli uprawnień.

Oprogramowanie to kompiluje się i działa na wielu systemach uniksowych
i jest kompatybilne z innymi print spoolami oraz drukarkami
sieciowymi, które używają interfejsu LPR oraz spełniają wymagania
RFC1179. LPRng dostarcza pakiety emulacyjne dla programów SVR4 lp oraz
lpstat, eliminując w ten sposób konieczność posiadania jeszcze jednego
pakietu print spoola. Te pakiety mogą być modyfikowane zgodnie z
lokalnymi wymaganiami.

Dla użytkowników, którzy potrzebują bezpiecznej i uwierzytelnianej
obsługi drukowania LPRng wspiera Kerberos V, MIT Kerberos IV Print
Support oraz PGP.

%description -l pt_BR.UTF-8
LPRng é uma versão melhorada, estendida e mais segura do gerenciador
de impressão LPR. Entre as melhorias se destacam: redirecionamento
dinâmico de filas de impressão, suspensão automática de trabalhos de
impressão, diagnóstico detalhado, várias impressoras por fila,
programas cliente não precisam ser SUID root e um mecanismo bastante
melhorado de permissões e autorizações.

%description -l ru.UTF-8
LPRng - это улучшенная, расширенная и портируемая реализация
функциональности спулера печати Berkeley LPR. Предоставляя тот же
интерфейс и отвечая всем требованиям RFC1179, эта реализация
совершенно новая и предоставляет поддержку следующих возможностей:
компактный (не требующий базы данных) lpr, программы lpc и lprm;
динамическая переадресация очередей печати; автоматическая
приостановка заданий; очень детальная диагностика; обслуживание одной
очереди несколькими принтерами; клиентские программы не должны быть
SUID root; сильно улучшенная система безопасности; сильно улучшенные
механизмы авторизации и прав доступа.

Программное обеспечение компиллируется и работает на большом
количестве UNIX-систем и совместимо с другими спулерами печати и
сетевыми принтерами, которые используют интерфейс LPR и отвечают
требованиям RFC1179. LPRng также предоставляет пакеты эмуляции для
программ SVR4 lp и lpstat, исключая потребность в другом пакете
спулера печати. Эти пакеты эмуляции могут быть модифицированы в
соответствии с локальными требованиями для поддержки антикварных
систем печати.

Для пользователей, которым нужна безопасная и/или аутентицируемая
поддержка печати, LPRng поддерживает Kerberos V, MIT Kerberos IV Print
Support и аутентикацию PGP. LPRng принят за стандарт в MIT для
использования в качестве системы поддержки печати в их кампусе.
Дополнительная поддержка аутентикации может быть добавлена без особых
усилий.

%description -l uk.UTF-8
LPRng - це покращена, розширена та портована реалізація функційності
спулеру друку Berkeley LPR. Надаючи той же інтерфейс та відповідаючи
усім вимогам RFC1179, ця реалізація абсолютно нова і надає підтримку
таких можливостей: компактний (не вимагаючий бази даних) lpr, програми
lpc та lprm; динамічна переадресація черг друку; автоматичне
призупинення завдань; дуже детальна діагностика; обслуговування одної
черги кількома прінтерами; клієнтські програми не повинні бути SUID
root; сильно покращена система безпеки; сильно покращені механізми
авторизації та прав доступу.

Програмне забезпечення компілюється та працює на великій кількості
UNIX-систем і сумісне з іншими спулерами друку та мережевими
прінтерами, котрі використовують інтерфейс LPR та відповідають вимогам
RFC1179. LPRng також надає пакети емуляції для програм SVR4 lp та
lpstat, виключаючи потребу в іншому пакеті спулера друку. Ці пакети
емуляции можуть бути модифіковані у відповідності з локальними
вимогами для підтримки антикварних систем друку.

Для користувачів, яким потрібна безпечна та/або аутентифікована
підтримка друку, LPRng підтримує Kerberos V, MIT Kerberos IV Print
Support та аутентикацію PGP. LPRng прийнято за стандарт в MIT для
використання в якості системи підтримки друку в їх кампусі. Додаткова
підтримка аутентикації може бути додана без особливих зусиль.

%prep
%setup -q -n lprng-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch8 -p1
%patch10 -p1

%{__rm} po/stamp-po

%build
%{__autoconf}
# now it wants to use /etc/lpd/lpd.{conf,perms} - stick to old values?
%configure \
	OPENSSL=/usr/bin/openssl \
	PSHOWALL="ax" \
	--enable-kerberos%{!?with_kerberos5:=no} \
	--enable-nls \
	--enable-ssl \
	--disable-static \
	--enable-tcpwrappers \
	--disable-werror \
	--with-userid=lp \
	--with-groupid=lp \
	--with-filterdir=%{lpfiltersdir} \
	--with-lockfile=%{_var}/spool/lpd/lpd \
	--with-lpd_conf_path=%{_sysconfdir}/lpd.conf \
	--with-lpd_perms_path=%{_sysconfdir}/lpd.perms \
	--with-done_jobs=0

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_var}/spool/lpd/lp} \
	$RPM_BUILD_ROOT%{_sysconfdir}/lpd/ssl.{ca,crl,server}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	POSTINSTALL="NO" \
	SAMPLESUFFIX=

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/pl/man1/monitor.1

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
%doc CHANGES CONTRIBUTORS COPYRIGHT ChangeLog LICENSE NEWS README README.SSL.SECURITY TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lpd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lpd.perms
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/printcap
%dir %{_sysconfdir}/lpd
# what perms?
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.ca
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.crl
%attr(750,root,lp) %dir %{_sysconfdir}/lpd/ssl.server
%attr(754,root,root) /etc/rc.d/init.d/lpd
%attr(755,root,root) %{_bindir}/cancel
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_sbindir}/checkpc
%attr(755,root,root) %{_sbindir}/lpc
%attr(755,root,root) %{_sbindir}/lpd
%attr(755,root,root) %{_sbindir}/lprng_certs
%attr(755,root,root) %{_sbindir}/lprng_index_certs
%dir %{lpfiltersdir}
%attr(755,root,root) %{lpfiltersdir}/lpbanner
%attr(755,root,root) %{lpfiltersdir}/lpf
%attr(755,root,root) %{lpfiltersdir}/pclbanner
%attr(755,root,root) %{lpfiltersdir}/psbanner
%dir %attr(750,root,lp) %{_var}/spool/lpd
%dir %attr(770,root,lp) %{_var}/spool/lpd/lp
%{_mandir}/man1/cancel.1*
%{_mandir}/man1/lp.1*
%{_mandir}/man1/lpbanner.1*
%{_mandir}/man1/lpf.1*
%{_mandir}/man1/lpq.1*
%{_mandir}/man1/lpr.1*
%{_mandir}/man1/lprm.1*
%{_mandir}/man1/lprng_certs.1*
%{_mandir}/man1/lprng_index_certs.1*
%{_mandir}/man1/lpstat.1*
%{_mandir}/man1/pclbanner.1*
%{_mandir}/man1/psbanner.1*
%{_mandir}/man5/lpd.conf.5*
%{_mandir}/man5/lpd.perms.5*
%{_mandir}/man5/printcap.5*
%{_mandir}/man8/checkpc.8*
%{_mandir}/man8/lpc.8*
%{_mandir}/man8/lpd.8*
%lang(pl) %{_mandir}/pl/man1/cancel.1*
%lang(pl) %{_mandir}/pl/man1/lp.1*
%lang(pl) %{_mandir}/pl/man1/lpbanner.1*
%lang(pl) %{_mandir}/pl/man1/lpf.1*
%lang(pl) %{_mandir}/pl/man1/lpq.1*
%lang(pl) %{_mandir}/pl/man1/lpr.1*
%lang(pl) %{_mandir}/pl/man1/lprm.1*
%lang(pl) %{_mandir}/pl/man1/lpstat.1*
%lang(pl) %{_mandir}/pl/man1/pclbanner.1*
%lang(pl) %{_mandir}/pl/man1/psbanner.1*
