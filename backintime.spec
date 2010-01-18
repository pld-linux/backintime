# TODO
# - add spec for kompare and add this app to Suggests in %{name}-kde4
#
Summary:	Back In Time is a simple backup tool for Linux
Summary(pl.UTF-8):	Back In Time to proste narzędzie do tworzenia kopii zapasowych pod Linuksem
Name:		backintime
Version:	0.9.26
Release:	1
License:	v2/GPL
Group:		Applications/Archiving
Source0:	http://backintime.le-web.org/download/backintime/%{name}-%{version}_src.tar.gz
Patch0:		%{name}_kde4_makefile.patch
URL:		http://backintime.le-web.org
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	which
Requires:	crondaemon
Requires:	python
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Back In Time is a simple backup tool for Linux inspired from "flyback
project" and "TimeVault". The backup is done by taking snapshots of a
specified set of directories. Currently there are two GUI available:
GNOME and KDE 4 (>= 4.1).

%description -l pl.UTF-8
Back In Time to proste narzędzie do tworzenia kopii zapasowych pod
Linuksem, zainspirowane narzędziami "flyback project" i "TimeVault".
Kopia jest wykonywana dla wskazanych katalogów. Aktualnie dostępne są
dwie wersje GUI: GNOME i KDE 4 (>= 4.1).

%package gnome
Summary:	GNOME GUI for Back In Time
Summary(pl.UTF-8):	GUI programu Back In Time przeznaczone dla środowiska GNOME
Group:		Applications/Archiving
Requires:	backintime
Requires:	python-gnome
Requires:	python-pygtk-glade
Suggests:	meld

%description gnome
Back In Time is a simple backup tool for Linux inspired from "flyback
project" and "TimeVault". The backup is done by taking snapshots of a
specified set of directories. Currently there are two GUI available:
GNOME and KDE 4 (>= 4.1).

%description gnome -l pl.UTF-8
Back In Time to proste narzędzie do tworzenia kopii zapasowych pod
Linuksem, zainspirowane narzędziami "flyback project" i "TimeVault".
Kopia jest wykonywana dla wskazanych katalogów. Aktualnie dostępne są
dwie wersje GUI: GNOME i KDE 4 (>= 4.1).

%package kde4
Summary:	KDE4 GUI for Back In Time
Summary(pl.UTF-8):	GUI programu Back In Time przeznaczone dla środowiska KDE4
Group:		Applications/Archiving
Requires:	backintime
Requires:	python-PyKDE4

%description kde4
Back In Time is a simple backup tool for Linux inspired from "flyback
project" and "TimeVault". The backup is done by taking snapshots of a
specified set of directories. Currently there are two GUI available:
GNOME and KDE 4 (>= 4.1).

%description kde4 -l pl.UTF-8
Back In Time to proste narzędzie do tworzenia kopii zapasowych pod
Linuksem, zainspirowane narzędziami "flyback project" i "TimeVault".
Kopia jest wykonywana dla wskazanych katalogów. Aktualnie dostępne są
dwie wersje GUI: GNOME i KDE 4 (>= 4.1).

%prep
%setup -q
# s/kde4/kde/
%patch0 -p0

%build
cd common
%configure
%{__make}
cd ../gnome
%configure \
	--no-check
cd ../kde4
%configure \
	--no-check

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C common install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C gnome install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C kde4 install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-common/copyright
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-gnome/copyright
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-kde4/copyright

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README TODO TRANSLATIONS VERSION common/debian_specific/copyright
%attr(755,root,root) %{_bindir}/backintime
%dir %{_datadir}/backintime
%dir %{_datadir}/backintime/common
%{_datadir}/backintime/common/*
%dir %{_datadir}/backintime/plugins
%{_datadir}/backintime/plugins/usercallbackplugin.py
%{_mandir}/man1/backintime.1*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/backintime-gnome
%{_datadir}/backintime/plugins/gnomeplugin.py
%dir %{_datadir}/backintime/gnome
%{_datadir}/backintime/gnome/*
%{_datadir}/gnome/help/backintime/
%dir %{_datadir}/omf/backintime
%{_datadir}/omf/backintime/backintime-C.omf
%{_desktopdir}/backintime-gnome*.desktop
%{_mandir}/man1/backintime-gnome.1*

%files kde4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/backintime-kde4
%{_datadir}/backintime/plugins/kde4plugin.py
%dir %{_datadir}/backintime/kde4
%{_datadir}/backintime/kde4/*
%dir %{_docdir}/kde/HTML/en/backintime
%{_docdir}/kde/HTML/en/backintime/*
%{_desktopdir}/kde4/backintime-kde4*.desktop
