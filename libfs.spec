%define major 6
%define libname %mklibname fs %{major}
%define devname %mklibname fs -d

Summary:	Library Interface to the X Font Server
Name:		libfs
Version:	1.0.10
Release:	1
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.xz
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)

%description
Libfs is a library interface to the X Font Server.

%package -n %{libname}
Summary:	Library Interface to the X Font Server
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Libfs is a library interface to the X Font Server.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}fs-static-devel < 1.0.4

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libFS-%{version}

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/doc/libFS/FSlib.txt

%files -n %{libname}
%{_libdir}/libFS.so.%{major}*

%files -n %{devname}
%doc doc/FSlib.txt
%{_libdir}/libFS.so
%{_libdir}/pkgconfig/libfs.pc
%{_includedir}/X11/fonts/FSlib.h
