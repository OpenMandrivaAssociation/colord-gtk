%define major 1
%define gi_major 1.0
%define libname %mklibname colord-gtk %major
%define develname %mklibname -d colord-gtk
%define girname %mklibname colord-gtk-gir %gi_major

%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		colord-gtk
Version:	0.3.1
Release:	4
Summary:	Library for the colord-gtk protocol
Group:		System/Libraries
License:	LGPLv2+
URL:		https://www.freedesktop.org/software/colord/
Source0:	https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0) >= 2.17.3
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.19.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(lcms2) >= 2.2
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	meson
BuildRequires:	docbook5-style-xsl

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package i18n
Summary:	Library for the colord-gtk protocol - translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %{libname}
Summary:	Library for the colord-gtk protocol
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for colord-gtk
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q
%autopatch -p1

%%build
%meson -Ddocs=true -Dgtk2=false -Dman=true -Dtests=false -Dvapi=true
%meson_build

%install
%meson_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%find_lang colord-gtk

%files i18n -f colord-gtk.lang

%files -n %{libname}
%{_bindir}/cd-convert
%{_libdir}/lib%{name}.so.%{major}*
%{_libdir}/libcolord-gtk4.so.%{major}*
%{_mandir}/man1/cd-convert.1.*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/colord-gtk
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/colord-gtk4.pc
%{_datadir}/gir-1.0/ColordGtk-%{gi_major}.gir
%{_datadir}/vala/vapi/colord-gtk.vapi
%{_datadir}/vala/vapi/colord-gtk.deps

%files -n %{girname}
%{_libdir}/girepository-1.0/ColordGtk-%{gi_major}.typelib
%exclude /usr/lib/debug/usr/bin/cd-convert-0.1.26-2.x86_64.debug
