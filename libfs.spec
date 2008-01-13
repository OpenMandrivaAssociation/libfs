%define name		libfs
%define version		1.0.0
%define release		%mkrel 5

%define libname		%mklibname fs 6
%define develname	%mklibname fs -d
%define staticname	%mklibname fs -s -d

Name: libfs
Summary:  Library Interface to the X Font Server
Version: 1.0.0
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
Library Interface to the X Font Server

#-----------------------------------------------------------

%package -n %{libname}
Summary:  Library Interface to the X Font Server
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
Library Interface to the X Font Server

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{mklibname fs 6 -d}

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libFS.so
%{_libdir}/libFS.la
%{_libdir}/pkgconfig/libfs.pc
%{_includedir}/X11/fonts/FSlib.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname fs 6 -s -d}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libFS.a

#-----------------------------------------------------------

%prep
%setup -q -n libFS-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libFS.so.6
%{_libdir}/libFS.so.6.0.0


