Summary:	A next-generation printing system for UNIX
Summary(pl):	System drukowania nowej generacji
Summary(pt_BR):	Gerenciador de impressЦo para UNIX e NT
Summary(ru):	Спулер печати LPRng
Summary(uk):	Спулер друку LPRng
Summary(zh_CN):	LPRng--╢Рс║ЁлпР
Name:		LPRng
Version:	3.8.21
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.lprng.com/pub/LPRng/LPRng/%{name}-%{version}.tgz
Source1:	%{name}.init
Source2:	%{name}.conf
Source3:	%{name}.printcap
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-lpd-perms.patch
Patch2:		%{name}-no_dupl_DESDIR.patch
Patch3:		%{name}-ngettext.patch
Patch4:		%{name}-missing-nls.patch
Patch5:		%{name}-pl.po.patch
URL:		http://www.astart.com/lprng/LPRng.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
PreReq:		rc-scripts >= 0.2.0
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	lpr
Obsoletes:	cups
Obsoletes:	cups-clients
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
LPRng jest rozszerzon╠, ulepszon╠ i portowaln╠ implementacj╠
Berkeley'owskiego LPR print spooler'a. Dostarcza ten sam interfejs
oraz jest zgodny z wymaganiami RFC1179. Jednocze╤nie wykonanie jest
caЁkowicie nowe i dostarcza nastЙpuj╠ce rzeczy:
- programy - "lekki" lpr (nie s╠ potrzebne ©adne bazy danych), lpc,
  oraz lprm;
- dynamiczna redyrekcja do kolejek;
- automatyczne wstrzymywanie zadaЯ;
- "gadatliwa" diagnostyka;
- obsЁugЙ wielu drukarek na jednej kolejce;
- programy klienckie nie musz╠ byФ SUID root;
- mocno rozszerzona kontrola bezpieczeЯstwa;
- mocno rozszerzone mechanizmy bezpieczeЯstwa i kontroli uprawnieЯ.

Oprogramowanie to kompiluje siЙ i dziaЁa na wielu systemach UNIX'owych
i jest kompatybilne z innymi print spoolami oraz drukarkami
sieciowymi, ktСre u©ywaj╠ interfejsu LPR oraz speЁniaj╠ wymagania
RFC1179. LPRng dostarcza pakiety emulacyjne dla programСw SVR4 lp oraz
lpstat, eliminuj╠c w ten sposСb konieczno╤Ф posiadania jeszcze jednego
pakietu print spoola. Te pakiety mog╠ byФ modyfikowane zgodnie z
lokalnymi wymaganiami.

Dla u©ytkownikСw, ktСrzy potrzebuj╠ bezpiecznej i autentyfikowanej
obsЁugi drukowania LPRng wspiera Kerberos V, MIT Kerberos IV Print
Support oraz PGP.

%description -l pt_BR
LPRng И uma versЦo melhorada, estendida e mais segura do gerenciador
de impressЦo LPR. Entre as melhorias se destacam: redirecionamento
dinБmico de filas de impressЦo, suspensЦo automАtica de trabalhos de
impressЦo, diagnСstico detalhado, vАrias impressoras por fila,
programas cliente nЦo precisam ser SUID root e um mecanismo bastante
melhorado de permissУes e autorizaГУes.

%description -l ru
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

%description -l uk
LPRng - це покращена, розширена та портована реал╕зац╕я функц╕йност╕
спулеру друку Berkeley LPR. Надаючи той же ╕нтерфейс та в╕дпов╕даючи
ус╕м вимогам RFC1179, ця реал╕зац╕я абсолютно нова ╕ нада╓ п╕дтримку
таких можливостей: компактний (не вимагаючий бази даних) lpr, програми
lpc та lprm; динам╕чна переадресац╕я черг друку; автоматичне
призупинення завдань; дуже детальна д╕агностика; обслуговування одно╖
черги к╕лькома пр╕нтерами; кл╕╓нтськ╕ програми не повинн╕ бути SUID
root; сильно покращена система безпеки; сильно покращен╕ механ╕зми
авторизац╕╖ та прав доступу.

Програмне забезпечення комп╕лю╓ться та працю╓ на велик╕й к╕лькост╕
UNIX-систем ╕ сум╕сне з ╕ншими спулерами друку та мережевими
пр╕нтерами, котр╕ використовують ╕нтерфейс LPR та в╕дпов╕дають вимогам
RFC1179. LPRng також нада╓ пакети емуляц╕╖ для програм SVR4 lp та
lpstat, виключаючи потребу в ╕ншому пакет╕ спулера друку. Ц╕ пакети
емуляции можуть бути модиф╕кован╕ у в╕дпов╕дност╕ з локальними
вимогами для п╕дтримки антикварних систем друку.

Для користувач╕в, яким потр╕бна безпечна та/або аутентиф╕кована
п╕дтримка друку, LPRng п╕дтриму╓ Kerberos V, MIT Kerberos IV Print
Support та аутентикац╕ю PGP. LPRng прийнято за стандарт в MIT для
використання в якост╕ системи п╕дтримки друку в ╖х кампус╕. Додаткова
п╕дтримка аутентикац╕╖ може бути додана без особливих зусиль.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/{config.,missing}* .
PSHOWALL="-ax"; export PSHOWALL
%configure \
	--disable-setuid \
	--with-userid=lp \
	--with-groupid=lp \
	--with-filterdir=%{_libdir}/lpfilters \
	--with-lockfile=%{_var}/spool/lpd/lpd \
	--with-done_jobs=0

%{__make}
%{__make} -C man

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_var}/spool/lpd/lp}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	POSTINSTALL="NO"
%{__make} install -C man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
# yes, overwrite distribution lpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lpd.conf
echo "default_printer = lp" >>$RPM_BUILD_ROOT%{_sysconfdir}/lpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/printcap
install lpd.perms $RPM_BUILD_ROOT%{_sysconfdir}
# default spool

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
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

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README HOWTO/LPRng-HOWTO.html
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lpd.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lpd.perms
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/printcap
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
