%define name zeitgeist
%define version 0.5.0
%define release %mkrel 1

Summary: Event logging framework for the desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/%name/0.5/%version/+download/%name-%version.tar.gz
License: LGPLv3
Group: System/Libraries
Url: http://launchpad.net/zeitgeist
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: intltool
BuildRequires: raptor
BuildRequires: python-rdflib
Requires: pygtk2.0
Requires: python-dbus
Requires: python-storm

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
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYRIGHT README NEWS
%_bindir/%name-daemon
%_bindir/%name-datahub
%py_puresitedir/%name
%_datadir/%name
%_datadir/dbus-1/services/org.gnome.zeitgeist.service
%_mandir/man1/%name-daemon.1*
%_mandir/man1/%name-datahub.1*
%_datadir/pkgconfig/zeitgeist-daemon.pc
