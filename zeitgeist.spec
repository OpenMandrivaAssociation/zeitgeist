%define api_version	2.0
%define gir_major       2.0
%define lib_major	0
%define lib_name        %mklibname %{name} %{api_version} %{lib_major}
%define libnamedev      %mklibname -d %{name} %{api_version} 
%define gir_name        %mklibname %{name}-gir %{gir_major}

Summary:	Event logging framework for the desktop
Name:		zeitgeist
Version:	1.0.3
Release:	1
Source0:	http://launchpad.net/%{name}/1.0/%{version}/+download/%{name}-%{version}.tar.xz
License:	LGPLv3
Group:		System/Libraries
Url:		http://launchpad.net/zeitgeist
BuildRequires:	pkgconfig(python3)
BuildRequires:	intltool
BuildRequires:	xapian-devel
BuildRequires:	raptor2
BuildRequires:	python-rdflib
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	vala-devel
Requires:	python3dist(pyxdg)
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

%package -n %{lib_name}
Summary: Libraries for %{name}
Group: System/Libraries

%description -n %{lib_name}
This package contains the libraries for %{name}.

%package -n %{gir_name}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}

%description -n %{gir_name}
GObject Introspection interface description for %{name}.

%package -n %libnamedev
Summary: Static libraries and header files of %{name}
Group:   Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}

%description -n %libnamedev
This package contains the header and pkg-config files for developing
with %{name}.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install pkgconfigdir=%{_datadir}/pkgconfig
rm -f %{buildroot}%{_mandir}/man1/%{name}-datahub.1*
rm -rf %{buildroot}%{_prefix}/doc/

%files
%doc AUTHORS NEWS
%{_bindir}/%{name}-daemon
%{_bindir}/%{name}-datahub
%{py_puresitedir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.Engine.service
%{_datadir}/%{name}
%{_userunitdir}/zeitgeist.service
%{_mandir}/man1/%{name}-daemon.1*
%{_sysconfdir}/xdg/autostart/%{name}-datahub.desktop
%{_datadir}/bash-completion/completions/%{name}-daemon

%files -n %{lib_name}
%{_libdir}/lib%{name}-%{api_version}.so.%{lib_major}
%{_libdir}/lib%{name}-%{api_version}.so.%{lib_major}.*

%files -n %{gir_name}
%{_libdir}/girepository-1.0/*-%{gir_major}.typelib

%files -n %{libnamedev}
%dir %{_includedir}/%{name}-%{api_version}
%{_includedir}/%{name}-%{api_version}/*.h
%{_libdir}/lib%{name}-%{api_version}.so
%{_datadir}/pkgconfig/%{name}-%{api_version}.pc
%{_datadir}/gir-1.0/*-%{gir_major}.gir
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps
