Summary:	Electronics schematics editor
Summary(pl.UTF-8):	Edytor schematów elektronicznych
Name:		geda-gschem
Version:	20061020
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.geda.seul.org/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c00d1692984d4fc89476beded6c2d571
URL:		http://www.geda.seul.org/
BuildRequires:	XFree86-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	guile-devel >= 1.4
BuildRequires:	libgdgeda-devel
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.sch	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# there is no reason to package gschem _source code_ documentation
rm -f $RPM_BUILD_ROOT%{_infodir}/gschemdoc*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO VOCAB*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/gEDA/bitmap
%{_datadir}/gEDA/gschem-*
%{_datadir}/gEDA/system-gschemrc
%{_datadir}/gEDA/scheme/*
%{_examplesdir}/%{name}-%{version}
