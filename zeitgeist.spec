Summary:	Event logging framework for the desktop
Name:		zeitgeist
Version:	0.9.5
Release:	1
Source0:	http://launchpad.net/%{name}/0.9/%{version}/+download/%{name}-%{version}.tar.bz2
License:	LGPLv3
Group:		System/Libraries
Url:		http://launchpad.net/zeitgeist
BuildRequires:	python-devel
BuildRequires:	xapian-devel
BuildRequires:	intltool
BuildRequires:	raptor
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	python-rdflib
Requires:	pygtk2.0
Requires:	python-dbus
Requires:	python-storm

%description
Zeitgeist is an "Event Logging Framework" that provides cross
application awareness of the desktop's activities.

You worked on a file, but you cannot remember where you saved it? You
visited a web page about basketball three days ago, but you cannot
find the URL in your browser's history? No problem, this is where
Zeitgeist enters the scene. It knows a lot about your activities and
has a feature rich D-Bus API which allows GUI applications like
gnome-zeitgeist, zeitgeistfs and others to present you your
activities in a readable way.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig
rm -f %{buildroot}%{_mandir}/man1/%{name}-datahub.1*
rm -rf %{buildroot}%{_prefix}/doc/

%files
%doc AUTHORS NEWS
%{_bindir}/%{name}-daemon
%{py_puresitedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/zeitgeist-fts
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_mandir}/man1/%{name}-daemon.1*
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.fts.service

