%define major 6
%define libname		%mklibname fs %{major}
%define develname	%mklibname fs -d

Name: libfs
Summary:  Library Interface to the X Font Server
Version: 1.0.3
Release: 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
Libfs is a library interface to the X Font Server.

%package -n %{libname}
Summary:  Library Interface to the X Font Server
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
Libfs is a library interface to the X Font Server.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}fs6-devel
Obsoletes: %{_lib}fs-static-devel

%description -n %{develname}
Development files for %{name}.

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%prep
%setup -qn libFS-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/doc/libFS/FSlib.txt

%files -n %{libname}
%doc doc/FSlib.txt
%{_libdir}/libFS.so.%{major}*

%files -n %{develname}
%{_libdir}/libFS.so
%{_libdir}/pkgconfig/libfs.pc
%{_includedir}/X11/fonts/FSlib.h

