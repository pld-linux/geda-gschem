Summary:	Electronics schematics editor
Summary(pl):	Edytor schematów elektronicznych
Name:		geda-gschem
Version:	20021103
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/devel/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.geda.seul.org/
BuildRequires:	libgdgeda-devel
BuildRequires:	libgeda-devel
BuildRequires:	geda-symbols
BuildRequires:	XFree86-devel
BuildRequires:	guile-devel >= 1.4
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	glib-devel >= 1.2.8
BuildRequires:	libpng-devel
BuildRequires:	libstroke-devel >= 0.4
Requires:	geda-symbols
Obsoletes:	gschem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gschem is an electronics schematic editor. It is part of the gEDA
project.

%description -l pl
Gschem to edytor schematów elektronicznych. Czê¶æ projektu gEDA.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install examples/*.sch	$RPM_BUILD_ROOT/usr/src/examples/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO VOCAB*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gEDA/bitmap/gschem*
%{_datadir}/gEDA/gschem-*
%{_datadir}/gEDA/system-gschemrc
%{_datadir}/gEDA/scheme
/usr/src/examples/%{name}
%{_infodir}/gschem*
