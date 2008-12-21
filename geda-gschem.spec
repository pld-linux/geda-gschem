Summary:	Electronics schematics editor
Summary(pl.UTF-8):	Edytor schematów elektronicznych
Name:		geda-gschem
Version:	1.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/release/v1.4/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	02a426cb537860bdf66d7c9b91cb7e04
URL:		http://www.geda.seul.org/
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	guile-devel >= 1.4
#BuildRequires:	libgdgeda-devel
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	libstroke-devel >= 0.4
BuildRequires:	pkgconfig
Requires:	geda-symbols >= %{version}
Requires:	libgeda >= %{version}
Obsoletes:	gschem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gschem is an electronics schematic editor. It is part of the gEDA
project.

%description -l pl.UTF-8
Gschem to edytor schematów elektronicznych. Część projektu gEDA.

%prep
%setup -q

%build
%configure \
	--disable-update-desktop-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.sch	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# there is no reason to package gschem _source code_ documentation
rm -f $RPM_BUILD_ROOT%{_infodir}/gschemdoc*

mv $RPM_BUILD_ROOT%{_localedir}/{nl_NL,nl}
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}
mv $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}
mv $RPM_BUILD_ROOT%{_localedir}/{ja_JP,ja}
mv $RPM_BUILD_ROOT%{_localedir}/{it_IT,it}
mv $RPM_BUILD_ROOT%{_localedir}/{fr_FR,fr}
rm -r $RPM_BUILD_ROOT%{_localedir}/af_ZA


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gEDA/bitmap
%{_datadir}/gEDA/gschem-*
%{_datadir}/gEDA/system-gschemrc
%{_datadir}/gEDA/scheme/*
%{_examplesdir}/%{name}-%{version}
