%define major		1
%define gi_major	1.0
%define libname		%mklibname colord-gtk %major
%define develname	%mklibname -d colord-gtk
%define girname		%mklibname colord-gtk-gir %gi_major

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		colord-gtk
Version:	0.1.25
Release:	2
Summary:	Library for the colord-gtk protocol
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.freedesktop.org/software/colord/
Source0:	http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0) >= 2.17.3
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.19.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(lcms2) >= 2.2
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	vala-tools

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
%apply_patches

%build
%configure2_5x --disable-static --enable-vala
%make

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%find_lang colord-gtk

%files i18n -f colord-gtk.lang

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/ColordGtk-%{gi_major}.gir
%{_datadir}/vala/vapi/colord-gtk.vapi

%files -n %{girname}
%{_libdir}/girepository-1.0/ColordGtk-%{gi_major}.typelib
