%define major		1
%define libname		%mklibname %{name} %{major}
%define girname		%mklibname %{name}-gir
%define develname	%mklibname %{name} -d

Name:		colord-gtk
Summary:	GTK support library for colord
Version:	0.1.23
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://
Source0:	http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
BuildRequires:	docbook-utils
BuildRequires:	gettext
BuildRequires:	glib2-devel
BuildRequires:	colord-devel >= %{version}
BuildRequires:	intltool
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	gobject-introspection-devel
BuildRequires:	vala-tools
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %{libname}

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Group:		Development/GNOME and GTK+
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure \
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
%doc %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/%{name}.vapi

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib
%{_datadir}/gir-1.0/ColordGtk-1.0.gir

%files -n %{develname}
%{_includedir}/colord-%{major}/%{name}*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
