%define api	1.0
%define major	1
%define libname	%mklibname %{name} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname %{name} -d

Name:		colord-gtk
Summary:	GTK support library for colord
Version:	0.1.24
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://
Source0:	http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
BuildRequires:	docbook-utils
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(lcms2)

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %{libname}
Summary:	GTK support library for colord
Suggests:	%{name}

%description -n %{libname}
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Obsoletes:	%{_lib}colord-gtk-gir < 0.1.24-1

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Group:		Development/GNOME and GTK+
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-gtk-doc \
	--disable-static \
	--disable-rpath \
	--disable-dependency-tracking
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files -n %{devname}
%{_includedir}/colord-%{major}/%{name}*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%doc %{_datadir}/gtk-doc/html/%{name}
#{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/gir-1.0/ColordGtk-1.0.gir

