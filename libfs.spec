%define libfs %mklibname fs 6
Name: libfs
Summary:  Library Interface to the X Font Server
Version: 1.0.0
Release: %mkrel 3
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

%package -n %{libfs}
Summary:  Library Interface to the X Font Server
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libfs}
Library Interface to the X Font Server

#-----------------------------------------------------------

%package -n %{libfs}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libfs} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libfs-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libfs}-devel
Development files for %{name}

%pre -n %{libfs}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libfs}-devel
%defattr(-,root,root)
%{_libdir}/libFS.so
%{_libdir}/libFS.la
%{_libdir}/pkgconfig/libfs.pc
%{_includedir}/X11/fonts/FSlib.h

#-----------------------------------------------------------

%package -n %{libfs}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libfs}-devel = %{version}
Provides: libfs-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libfs}-static-devel
Static development files for %{name}

%files -n %{libfs}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libfs}
%defattr(-,root,root)
%{_libdir}/libFS.so.6
%{_libdir}/libFS.so.6.0.0


